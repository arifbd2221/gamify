from django.db import models
from django.contrib.auth import get_user_model


class MaxScore(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    score = models.PositiveIntegerField(null=False, blank=False)
    game = models.CharField(max_length=16, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user.phone} {self.game} {self.score}"

