from django.urls import path 
from . import views 

urlpatterns = [
    path('move_piece/', views.move_piece)
]