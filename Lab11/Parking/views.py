from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.views import View

from Parking import models, forms


class Home(View):
    def get(self, request):
        ticket = list(models.Ticket.objects.all().values_list("location", flat=True))
        ticket2 = list(models.Ticket.objects.all().values_list("datetime", flat=True))
        ticket3 = zip(ticket, ticket2)
        return render(request, 'index2.html', {"form": forms.TicketDisplayForm(), "ticket3": ticket3})

    def post(self, request):
        form = forms.TicketForm(request.POST)
        if form.is_valid():
            form.save()
            form = forms.TicketForm()
        ticket = list(models.Ticket.objects.all().values_list('location', flat=True))
        ticket2 = list(models.Ticket.objects.all().values_list('datetime', flat=True))
        ticket3 = zip(ticket, ticket2)
        return render(request, 'index2.html', {"form": form, "ticket3": ticket3})
