from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_response, name='boards_home_page'),
    path('<str:board_name>/',views.board_topics, name="board_topics"),
    path('<str:board_name>/add_new/',views.add_topic, name="add_topic")
]