from django.contrib import admin

from .models import Ticket, TicketComment, AdminTicket

admin.site.register(Ticket)
admin.site.register(TicketComment)
admin.site.register(AdminTicket)
