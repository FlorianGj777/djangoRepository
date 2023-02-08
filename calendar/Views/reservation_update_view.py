from django.urls import reverse
from django.views.generic import UpdateView

from calendar.Models.reservation import Reservation


class ReservationUpdateView(UpdateView):
    template_name = 'reservation_update_view.html'
    model = Reservation
    fields = ['date']

    def get_success_url(self):
        return reverse('calendar_list')
