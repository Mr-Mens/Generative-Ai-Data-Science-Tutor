from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat_view'),
    path('tutor_response/', views.tutor_response, name='tutor_response'),
]
