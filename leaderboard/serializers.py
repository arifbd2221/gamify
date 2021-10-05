from rest_framework import serializers
from leaderboard.models import MaxScore

class MaxScoreSerializer(serializers.ModelSerializer):
    rank = serializers.IntegerField(read_only=True, default=None)
    phone = serializers.SerializerMethodField(read_only=True)
    fullname = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = MaxScore
        # Tuple of serialized model fields (see link [2])
        exclude = ['id', 'user']
    
    def get_phone(self, obj):
        return obj.user.phone
    
    def get_fullname(self, obj):
        return obj.user.fullname