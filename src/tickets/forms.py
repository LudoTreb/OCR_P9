"""
The form for the ticket.
"""
from django import forms

from tickets.models import Ticket


class TicketForm(forms.ModelForm):
    """
    the ticket's form whith fields : title, description and image.
    """

    ticket_update = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        """
        The different fields for ticket: title, description and image.
        """

        model = Ticket
        fields = [
            "title",
            "description",
            "image",
        ]


class DeleteTicketForm(forms.Form):
    """
    The ticket's delete form.
    """

    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
