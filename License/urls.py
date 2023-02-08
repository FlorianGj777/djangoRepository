"""License URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from calendar.Views.Reservation_form import ReservationFormView
from calendar.Views.index_view import IndexView
from calendar.Views.register_form import RegisterFormView
from calendar.Views.reservation_delete_view import ReservationDeleteView
from calendar.Views.reservation_list_view import ReservationListView
from calendar.Views.reservation_update_view import ReservationUpdateView

from calendar.Views.login_view import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    #Rest framework pour le json
    path('register', RegisterFormView.as_view(), name='register_form_view'),
    path('login', LoginView.as_view(), name='login_view'),
    path('logout', LogoutView.as_view(next_page='register_form_view'), name='logout_view'),

    #calendar
    path('date/update/<int:pk>', ReservationUpdateView.as_view(), name='calendar_update'),
    path('date/delete/<int:pk>', ReservationDeleteView.as_view(), name='calendar_delete'),
    path('date/list', ReservationListView.as_view(), name='calendar_list'),
    path('date', ReservationFormView.as_view(), name='date')
]


