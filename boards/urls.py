from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_response, name='home_response'),
    path('<int:board_id>/',views.board_topics, name="board_topics")
]