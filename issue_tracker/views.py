from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator


from .models import Ticket, TicketComment, AdminTicket

#Home page will show all the open tickets (no login required)
def home(request):
    tickets = Ticket.objects.all().order_by('-date_added')
    paginator = Paginator(tickets,10) # Show 2 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'issue_tracker/home.html', context)

def ticket_comment(request, ticket_id):
    tickets = Ticket.objects.filter(id=ticket_id)
    context = {'tickets': tickets}
    return render(request, 'issue_tracker/ticket_comment.html', context)
