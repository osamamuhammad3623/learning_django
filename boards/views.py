from pydoc_data.topics import topics
from django.shortcuts import render
from django.http import HttpResponse
from .models import Board, Topic

def home_response(request):
    # to get Board objects from DB
    boards = Board.objects.all()

    return render(request, 'home.html', {'boards': boards})


def board_topics(request, board_id):
    selected_board = Board.objects.get(board_pk=board_id)
    #board_topics = Topic.objects.get(board=selected_board)
    print(selected_board)
    
    return render(request, 'topics.html', {'board': selected_board.name})