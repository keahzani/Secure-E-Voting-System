from django.urls import path
from . import views

urlpatterns = [
    path('<int:election_id>/', views.cast_vote, name='cast_vote'),
    path('<int:election_id>/results/', views.election_results, name='election_results'),
    path('cast-vote/<int:election_id>/', views.vote_view, name='cast_vote'),
    path('election/<int:election_id>/results/', views.results_view, name='results'),
]
