from django.urls import path
from . import views

urlpatterns = [
    path('', views.election_list, name='election_list'),
]
