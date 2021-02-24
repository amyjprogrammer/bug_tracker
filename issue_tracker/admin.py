from django.contrib import admin

from .models import Ticket, TicketComment, AdminTicket

admin.site.site_header= "Bug Tracker"
admin.site.title= 'Admin Bug Tracker'

class InlineTicketComment(admin.StackedInline):
    model = TicketComment
    extra = 3

class InlineAdminTicket(admin.StackedInline):
    model = AdminTicket


class TicketAdmin(admin.ModelAdmin):
    inlines = [ InlineAdminTicket, InlineTicketComment,]
    list_display = ('title', 'issue_description','ticket_choice')
    list_filter = ('ticket_choice',)
    search_fields = ('title','issue_description')

admin.site.register(Ticket, TicketAdmin)
