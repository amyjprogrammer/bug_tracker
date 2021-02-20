import django_filters
from django_filters import CharFilter

from .models import Ticket

class TicketFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr= 'icontains')
    issue_description = CharFilter(field_name="issue_description", lookup_expr= 'icontains')
    class Meta:
        model = Ticket
        fields = ['title', 'issue_description', 'ticket_choice']
