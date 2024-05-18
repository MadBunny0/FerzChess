from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home),
    path('process_positions/', views.process_positions),
    path('move_piece/', views.move_piece)
]