from django.contrib import admin

# Register your models here.
from tickets.models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'time_created')


admin.site.register(Ticket, TicketAdmin)
