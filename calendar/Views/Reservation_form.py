from django.contrib import messages
from django.http import request
from django.urls import reverse
from django.views import generic

from calendar.Models.reservation import Reservation
from calendar.forms.reservation import ReservationForm


class ReservationFormView(generic.FormView):
    template_name = 'reservation_form.html'
    form_class = ReservationForm

    def form_valid(self, form):
        user = self.request.user
        date = form.cleaned_data['date']
        dateDay = date.today()
        if date <= dateDay:
            messages.error(self.request, "Veulliez choisir une date ultérieur à la date du jour")
            return super().form_invalid(form)
        for reservation in user.reservations.all():
            if reservation.date == date:
                messages.error(self.request, "Date déja prise")
                return super().form_invalid(form)
        Reservation.objects.create(personne=user, date=date)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('calendar_list')