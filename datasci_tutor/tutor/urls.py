from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.tutor_response, name='tutor_response'),
]
