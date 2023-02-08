from django.urls import reverse
from django.views.generic import DeleteView

from calendar.Models.reservation import Reservation


class ReservationDeleteView(DeleteView):
    template_name = 'reservation_delete_view.html'
    model = Reservation
    fields = ['date']

    def get_success_url(self):
        return reverse('calendar_list')
