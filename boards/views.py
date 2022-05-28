from pydoc_data.topics import topics
from django.shortcuts import render,get_object_or_404, redirect
from matplotlib.pyplot import title
from django.contrib.auth.models import User
from .models import *

def home_response(request):
    # to get Board objects from DB
    boards = Board.objects.all()

    return render(request, 'home.html', {'boards': boards})


def board_topics(request, board_name):
    # get board info
    selected_board = get_object_or_404(Board, name=board_name)
    # get topics of that board
    board_topics = Topic.objects.filter(board = selected_board.board_pk)

    return render(request, 'topics.html', {'board': selected_board.name, 'topics': board_topics})

def add_topic(request,board_name):
    selected_board = get_object_or_404(Board, name=board_name)

    if request.method == 'POST':
        topic_title = request.POST['title']
        desc = request.POST['message']

        t = Topic.objects.create(
            title = topic_title,
            topic_desc = desc,
            board = selected_board,
            author = User.objects.first()
        )

        return redirect('board_topics', board_name=selected_board.name)
    
    return render(request, 'add_topic.html', {'board': selected_board.name})
