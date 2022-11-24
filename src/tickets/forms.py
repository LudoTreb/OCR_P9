from django import forms

from tickets.models import Ticket


class TicketForm(forms.ModelForm):
    ticket_update = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image', ]


class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
