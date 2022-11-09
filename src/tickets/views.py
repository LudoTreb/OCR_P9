from django.shortcuts import render, redirect

# Create your views here.
from tickets.forms import TicketForm
from tickets.models import Ticket


def ticket_add(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            return redirect('ticket-detail', ticket.id)
    else:
        form = TicketForm()
    return render(request, 'ticket_add.html', {'form': form})


def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'ticket_detail.html', context={'ticket': ticket})


def tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets.html', context={'tickets': tickets})
