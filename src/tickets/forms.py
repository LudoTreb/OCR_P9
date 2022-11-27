from django import forms

from tickets.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        # TODO: explicit fields instead of __all__
        fields = '__all__'
