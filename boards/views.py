from pydoc_data.topics import topics
from django.shortcuts import render
from .models import *

def home_response(request):
    # to get Board objects from DB
    boards = Board.objects.all()

    return render(request, 'home.html', {'boards': boards})


def board_topics(request, board_name):
    # get board info
    selected_board = Board.objects.get(name=board_name)
    # get topics of that board
    board_topics = Topic.objects.filter(board = selected_board.board_pk)

    return render(request, 'topics.html', {'board': selected_board.name, 'topics': board_topics})