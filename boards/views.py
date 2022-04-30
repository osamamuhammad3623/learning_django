from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

def home_response(request):
    # to get Board objects from DB
    boards = Board.objects.all()

    return render(request, 'home.html', {'boards': boards})
