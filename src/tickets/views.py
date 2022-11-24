from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from tickets import models, forms
from tickets.forms import TicketForm
from tickets.models import Ticket


def ticket_add(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('ticket-detail', ticket.id)
    else:
        ticket_form = TicketForm()
    return render(request, 'ticket_add.html', context={'form': ticket_form})


def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'ticket_detail.html', context={'ticket': ticket})


def tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets.html', context={'tickets': tickets})


# def ticket_update(request, ticket_id):
#     ticket = Ticket.objects.get(id=ticket_id)
#     if request.method == 'POST':
#         ticket_update_form = TicketForm(request.POST, instance=ticket)
#         if ticket_update_form.is_valid():
#             ticket_update_form.save()
#             return redirect('ticket-detail', ticket.id)
#
#     else:
#         ticket_update_form = TicketForm(instance=ticket)
#
#     return render(request, 'ticket_update.html', context={
#                                                 'ticket_update_form': ticket_update_form,
#                                             })

def ticket_update(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    update_form = forms.TicketForm(instance=ticket)
    delete_form = forms.DeleteTicketForm()
    if request.method == 'POST':
        if 'ticket_update' in request.POST:
            update_form = forms.TicketForm(request.POST, request.FILES, instance=ticket)
            if update_form.is_valid():
                update_form.save()
                return redirect('posts')
        if 'delete_ticket' in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect('posts')
    context = {
        'update_form': update_form,
        'delete_form': delete_form,
    }
    return render(request, 'ticket_update.html', context=context)
