from django.shortcuts import render, redirect

# Create your views here.
from tickets.forms import TicketForm
from tickets.models import Ticket


def ticket_add(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST)
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

