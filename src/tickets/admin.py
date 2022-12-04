"""
The ticket for administrator.
"""
from django.contrib import admin

from tickets.models import Ticket


class TicketAdmin(admin.ModelAdmin):
    """
    The ticket's model for the administrator. Whith the field: title, description and time_created.
    """

    list_display = ("title", "description", "time_created")


admin.site.register(Ticket, TicketAdmin)
