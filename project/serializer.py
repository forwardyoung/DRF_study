from .models import Participation
from rest_framework import serializers

class ParticipationSerializer(serializers.Serializer):
    class Meta:
        model = Participation
        fields = '__all__'