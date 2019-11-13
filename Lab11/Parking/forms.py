from django.forms import ModelForm
from Parking import models


class TicketForm(ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['location', 'datetime']


class TicketDisplayForm(ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['location', 'datetime']
