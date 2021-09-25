from django.urls import path
from leaderboard.views import MaxScoreView, LeaderboardView
urlpatterns = [
    path('score', MaxScoreView.as_view(), name='score'),
    path('list', LeaderboardView.as_view(), name='list'),
]