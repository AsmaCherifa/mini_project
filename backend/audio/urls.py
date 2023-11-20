from django.urls import path
from .views import LoginAPIView,RegisterAPIView,AudioAPIView,TranscriptionView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('audio/', AudioAPIView.as_view(), name='audio'),
    path('transcription/', TranscriptionView.as_view(), name='transcription'),
    path('addAudio/', AudioAPIView.as_view(), name='add-audio'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
