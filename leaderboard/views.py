from leaderboard.serializers import MaxScoreSerializer
from rest_framework import generics, status, views
from rest_framework.response import Response
from leaderboard.models import MaxScore
from django.db.models import F
from django.db.models.expressions import Window
from django.db.models.functions import RowNumber
from rest_framework.permissions import IsAuthenticated

class MaxScoreView(views.APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        score = request.data.get('score')
        game = request.data.get('game')
        max_score = MaxScore.objects.filter(
            user=request.user,
            game=game
        )
        
        if max_score.exists():
            max_score = max_score.first()
            if max_score.score < score:
                max_score.score = score
                max_score.save()
        else:
            MaxScore.objects.create(
                user=request.user,
                score=score,
                game=game
            )
        return Response("Successfully Created", status=201)


class LeaderboardView(generics.ListAPIView):
    serializer_class = MaxScoreSerializer
    
    def get_queryset(self):
        score_list = MaxScore.objects.filter(score__gt=0).annotate(
                    rank=Window(
                        expression=RowNumber(),
                        order_by=(
                            F('score').desc(),
                            F('id').asc(),
                        ),
                    )
        ).order_by('rank')[:100]
        
        return score_list