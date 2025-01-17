from django.urls import path , include
from . import views 
urlpatterns = [
     path('chat/', views.home, name='chat'),
     path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
     path('404/', views.error_404, name='404'),
]