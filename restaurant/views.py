from django.shortcuts import render

# Create your views here.


def get_homepage(request):
    return render(request, 'restaurant/homepage.html')
