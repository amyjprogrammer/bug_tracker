from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from .filters import TicketFilter
from .models import Ticket, TicketComment, AdminTicket
from .forms import TicketForm, TicketCommentForm, AdminTicketForm

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
def admin_dashboard(request):
    """page for admin to see all issues and info"""
    tickets = Ticket.objects.all()

    context= {'tickets': tickets}
    return render(request, 'issue_tracker/admin_dashboard.html', context)
