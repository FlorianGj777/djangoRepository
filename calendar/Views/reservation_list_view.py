from django.views.generic import ListView

from calendar.Models.reservation import Reservation


class ReservationListView(ListView):
    template_name = 'reservation_list.html'
    model = Reservation
