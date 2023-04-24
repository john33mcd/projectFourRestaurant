from django.shortcuts import render
from .models import Reservation

# Create your views here.


def get_homepage(request):
    return render(request, 'restaurant/homepage.html')


def get_reservation(request):
    return render(request, 'restaurant/reservation.html')
