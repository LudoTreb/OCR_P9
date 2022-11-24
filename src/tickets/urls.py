from django.urls import path

from tickets.views import ticket_add, ticket_detail, ticket_update

urlpatterns = [
    path("ticket/add/", ticket_add, name="ticket-add"),
    path("ticket/<int:ticket_id>/", ticket_detail, name="ticket-detail"),
    path('ticket/<int:ticket_id>/update', ticket_update, name='ticket-update'),
]
