"""Entering the bug info and having the Admin set status and priority"""

import datetime
from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    ticket_author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    ticket_choices = [
        ('Bug', 'Bug'),
        ('Enhancement', 'Enhancement'),
        ('New_Feature', 'New Feature'),
    ]
    ticket_choice = models.CharField(max_length=20, choices=ticket_choices, default='Bug')
    issue_description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def get_ticket_author(self):
        return self.ticket_author

class TicketComment(models.Model):
    comment = models.ForeignKey(Ticket, on_delete=models.CASCADE,  related_name='comments')
    comment_author = models.CharField(max_length=75)
    comment_text = models.CharField(max_length=550)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment_text[:50]}..."

class AdminTicket(models.Model):
    #allows the admin to assign a priority and status to the ticket
    admin_ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE, related_name ='admin')
    priority_choices =[
        ("Critical", 'Critical'),
        ('High', 'High'),
        ('Normal', 'Normal'),
    ]
    priority_choice = models.CharField(max_length=10, choices=priority_choices, blank=True, null=True)
    status_choices =[
        ('Open', 'Open'),
        ('Pending', 'Pending'),
        ('Closed', 'Closed'),
    ]
    status_choice = models.CharField(max_length=10, choices=status_choices, blank=True, null=True)
    additional_comments = models.CharField(max_length=350, blank=True, null=True)
