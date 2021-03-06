from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from .filters import TicketFilter, AdminTicketFilter, TicketCommentFilter
from .models import Ticket, TicketComment, AdminTicket
from .forms import TicketForm, TicketCommentForm, AdminTicketForm
from .decorators import allowed_users, admin_only


#Home page will show all the open tickets (no login required)
def home(request):
    tickets = Ticket.objects.all().order_by('-date_added')
    myFilter = TicketFilter(request.GET, queryset=tickets)
    tickets = myFilter.qs
    paginator = Paginator(tickets,10) # Show 10 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'tickets': tickets, 'myFilter': myFilter}
    return render(request, 'issue_tracker/home.html', context)

#no login required to view the ticket and comments
def ticket_comment(request, ticket_id):
    """show all the comments with one ticket"""
    tickets = Ticket.objects.filter(id=ticket_id)
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket_comments = ticket.comments.all().order_by('-created_date')
    paginator = Paginator(ticket_comments, 10) # Show 10 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'tickets': tickets, 'page_obj' : page_obj, 'ticket':ticket}
    return render(request, 'issue_tracker/ticket_comment.html', context)

#no login required to add a comment
def add_ticket_comment(request, ticket_id):
    """adding a comment form"""
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method != "POST":
        #no data showing; create a blank form
        form = TicketCommentForm()
    else:
        #adding a new comment
        form = TicketCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment = ticket
            comment.save()
            return redirect('issue_tracker:ticket_comment', ticket_id=ticket.id)

    context= {'form': form, 'ticket': ticket}
    return render(request, 'issue_tracker/add_ticket_comment.html', context)

@login_required
@admin_only
def admin_dashboard(request):
    """page for admin to see all issues and info"""
    tickets = Ticket.objects.all().order_by('-date_added')
    myFilter = AdminTicketFilter(request.GET, queryset=tickets)
    tickets = myFilter.qs
    ticket_comments = TicketComment.objects.all().order_by('-created_date')
    myCommentFilter = TicketCommentFilter(request.GET, queryset=ticket_comments)
    ticket_comments = myCommentFilter.qs
    admin_tickets = AdminTicket.objects.all()
    paginator = Paginator(ticket_comments, 10) # Show 10 contacts per page.
    paginators = Paginator(tickets, 10) # Show 10 contacts per page.

    page_number = request.GET.get('page')
    page_number1 = request.GET.get('page1')
    page_obj = paginator.get_page(page_number)
    page_objs = paginators.get_page(page_number)

    open_admin = AdminTicket.objects.filter(status_choice = 'Open')
    open_tickets = open_admin.count()
    open_critical_tickets = open_admin.filter(priority_choice='Critical').count()

    pending_admin = AdminTicket.objects.filter(status_choice = 'Pending')
    pending_tickets = pending_admin.count()
    pending_critical_tickets = pending_admin.filter(priority_choice='Critical').count()

    critical_sum = open_critical_tickets + pending_critical_tickets

    context= {'page_objs': page_objs, 'page_obj': page_obj, "admin_tickets": admin_tickets, 'open_tickets': open_tickets, 'pending_tickets': pending_tickets, 'open_critical_tickets' : open_critical_tickets, 'pending_critical_tickets': pending_critical_tickets, 'critical_sum': critical_sum, 'myFilter': myFilter, 'myCommentFilter': myCommentFilter}
    return render(request, 'issue_tracker/admin_dashboard.html', context)

@login_required
def user_page(request):
    """login page for customer"""
    tickets = Ticket.objects.filter(ticket_author=request.user).order_by('-date_added')
    myFilter = TicketFilter(request.GET, queryset=tickets)
    tickets = myFilter.qs

    context = {"tickets": tickets, "myFilter": myFilter}
    return render(request, 'issue_tracker/user_page.html', context)

@login_required
def create_ticket(request):
    """create new bug ticket"""
    if request.method != 'POST':
        #blank form
        form = TicketForm()
    else:
        form = TicketForm(request.POST)
        if form.is_valid():
            add_ticket = form.save(commit=False)
            add_ticket.ticket_author = request.user
            add_ticket.save()
            return redirect('issue_tracker:admin_dashboard')

    context = {'form': form}
    return render(request, 'issue_tracker/create_ticket.html', context)

@login_required
@allowed_users(allowed_groups=['admin'])
def add_admin_ticket(request, ticket_id):
    """add admin info like priority and status"""
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method != 'POST':
        #blank form
        admin_form = AdminTicketForm()
        #show ticket info
        ticket_form = TicketForm(instance=ticket)
    else:
        #updating the status and priority
        admin_form = AdminTicketForm(request.POST)
        ticket_form = TicketForm(request.POST, instance=ticket)

        if admin_form.is_valid() and ticket_form.is_valid():
            add_ticket = admin_form.save(commit=False)
            add_ticket.admin_ticket = ticket
            add_ticket.save()
            ticket_form.save()
            messages.success(request, f'You have updated the ticket.')
            return redirect('issue_tracker:admin_dashboard')

    context = {'ticket': ticket, 'admin_form': admin_form, 'ticket_form': ticket_form}
    return render(request, 'issue_tracker/add_admin_ticket.html', context)

@login_required
@allowed_users(allowed_groups=['admin'])
def edit_admin_ticket(request, ticket_id, admin_id):
    """Update both the admin and ticket info"""
    ticket = get_object_or_404(Ticket, id=ticket_id)
    admin = get_object_or_404(AdminTicket, id=admin_id)
    if request.method != 'POST':
        #show admin info
        admin_form = AdminTicketForm(instance=admin)
        #show ticket info
        ticket_form = TicketForm(instance=ticket)
    else:
        #updating both ticket and admin info
        admin_form = AdminTicketForm(request.POST, instance=admin)
        ticket_form = TicketForm(request.POST, instance=ticket)

        if admin_form.is_valid() and ticket_form.is_valid():
            admin_form.save()
            ticket_form.save()
            messages.success(request, f'You have updated the ticket.')
            return redirect('issue_tracker:admin_dashboard')

    context = {'ticket': ticket, 'admin_form': admin_form, 'ticket_form': ticket_form, 'admin': admin}
    return render(request, 'issue_tracker/edit_admin_ticket.html', context)

@login_required
def edit_ticket(request, ticket_id):
    """edit bug ticket"""
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method != 'POST':
        #show previous info
        form = TicketForm(instance=ticket)
    else:
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('issue_tracker:admin_dashboard')

    context = {'form': form, 'ticket': ticket}
    return render(request, 'issue_tracker/edit_ticket.html', context)

@login_required
@allowed_users(allowed_groups=['admin'])
def delete_ticket(request, ticket_id):
    """option to delete a ticket, but will take you to a page to make sure"""
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == "POST":
        ticket.delete()
        messages.success(request, f'You have deleted the ticket.')
        return redirect('issue_tracker:admin_dashboard')

    context = {"ticket": ticket}
    return render(request, 'issue_tracker/delete_ticket.html', context)

@login_required
@allowed_users(allowed_groups=['admin'])
def delete_comment(request, comment_id):
    """Delete a comment"""
    comment = get_object_or_404(TicketComment, id=comment_id)

    if request.method == "POST":
        comment.delete()
        context = {'comment': comment}
        return redirect('issue_tracker:admin_dashboard')
