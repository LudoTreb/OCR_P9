"""
Views for the ticket.
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from tickets import models, forms
from tickets.forms import TicketForm
from tickets.models import Ticket


@login_required
def ticket_add(request):
    """
    Display a form's ticket.  The user can input the all ticket's fields.

    **Context**
    ``ticket_form``
        An instance of : `TicketForm()`.

    **Template:**
    template: `ticket_add.html'
    """
    if request.method == "POST":
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("ticket-detail", ticket.id)
    else:
        ticket_form = TicketForm()
    return render(request, "ticket_add.html", context={"form": ticket_form})


@login_required
def ticket_detail(request, ticket_id):
    """
    Display a ticket's detail by is id.

    **Context**
    ``ticket``
        A Queryset of : Ticket.objects.get(id=ticket_id).

    **Template:**
    template: `ticket_detail.html'
    """
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, "ticket_detail.html", context={"ticket": ticket})


@login_required
def tickets(request):
    """
    A Queryset of : Ticket.objects.all().
    """
    context = {"ticket": Ticket.objects.all()}
    return render(request, "tickets.html", context=context)


@login_required
def ticket_update(request, ticket_id):
    """
    Display an existing form's ticket by his id.
    The user can update, change or delete the ticket.

    **Context**
    ``update_form``
        An instance of : `forms.TicketForm(instance=ticket)`.
    ``delete_form``
        An instance of : `forms.DeleteReviewForm()`.

    **Template:**
    template: `ticket_update.html'
    """
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    update_form = forms.TicketForm(instance=ticket)
    delete_form = forms.DeleteTicketForm()
    if request.method == "POST":
        if "ticket_update" in request.POST:
            update_form = forms.TicketForm(request.POST, request.FILES, instance=ticket)
            if update_form.is_valid():
                update_form.save()
                return redirect("posts")
        if "delete_ticket" in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect("posts")
    context = {
        "update_form": update_form,
        "delete_form": delete_form,
    }
    return render(request, "ticket_update.html", context=context)
