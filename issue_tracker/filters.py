import django_filters
from django_filters import CharFilter

from .models import Ticket, TicketComment

class TicketFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr= 'icontains')
    issue_description = CharFilter(field_name="issue_description", lookup_expr= 'icontains')
    class Meta:
        model = Ticket
        fields = ['title', 'issue_description', 'ticket_choice']


class AdminTicketFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr= 'icontains')

    class Meta:
        model = Ticket
        fields = ['title', 'ticket_choice']


class TicketCommentFilter(django_filters.FilterSet):
    comment_text = CharFilter(field_name="comment_text", lookup_expr="icontains")
    comment_text = django_filters.CharFilter(label="Comment:")
    class Meta:
        model = TicketComment
        fields = ['comment_text', ]
