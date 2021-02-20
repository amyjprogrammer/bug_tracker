from django import forms

from .models import Ticket, TicketComment, AdminTicket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ['ticket_author', 'date_added']


class TicketCommentForm(forms.ModelForm):
    comment_text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = TicketComment
        fields = ['comment_author', 'comment_text']
        labels = {
            'comment_author': 'Author',
            'comment_text': 'Comment',
        }


class AdminTicketForm(forms.ModelForm):
    class Meta:
        model = AdminTicket
        fields = '__all__'
        exclude = ['admin_ticket']
