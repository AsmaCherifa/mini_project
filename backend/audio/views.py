from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Annotator,Audio,Transcription
from .serializers import AnnotatorSerializer,AudioSerializer,TranscriptionSerializer

#Login
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            annotator = Annotator.objects.get(username=username, password=password)
        except Annotator.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = AnnotatorSerializer(annotator)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
#Register
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = AnnotatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Audio API: list all audios
class AudioAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Audio.objects.filter(status='available')
        serializer = AudioSerializer(queryset, many=True)
        return Response(serializer.data)


class TranscriptionView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TranscriptionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                audio_id = request.data.get('audio_id')
                audio = Audio.objects.get(id=audio_id)
            except Audio.DoesNotExist:
                print("Audio not found for ID: {audio_id}")

            audio.status = 'submitted'
            audio.save()

            transcription = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)