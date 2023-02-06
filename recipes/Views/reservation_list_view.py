from django.views.generic import ListView

from recipes.Models.reservation import Reservation


class ReservationListView(ListView):
    template_name = 'reservation_list.html'
    model = Reservation
