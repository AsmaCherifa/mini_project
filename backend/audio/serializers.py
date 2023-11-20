from rest_framework import serializers
from .models import Annotator,Audio,Transcription
class AnnotatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotator
        fields = ('id', 'username', 'password')


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = '__all__'

class TranscriptionSerializer(serializers.ModelSerializer):
    audio_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Transcription
        fields = ('annotator', 'text', 'audio_id')