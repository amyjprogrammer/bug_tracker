from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Ticket, AdminTicket

#create AdminTicket for each new Ticket
@receiver(post_save, sender=Ticket)
def create_adminticket(sender, instance, created, **kwargs):
    if created:
        AdminTicket.objects.create(ticket=instance)

#save AdminTicket when Ticket is saved
@receiver(post_save, sender=Ticket)
def save_adminticket(sender, instance, created, **kwargs):
    instance.adminticket.save()
