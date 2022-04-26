from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

def home_response(request):
    # to get Board objects from DB
    boards = Board.objects.all()
    
    names_str = ""
    for b in boards:
        names_str += b.name + " "
    return HttpResponse(f"Available boards: {names_str}")
