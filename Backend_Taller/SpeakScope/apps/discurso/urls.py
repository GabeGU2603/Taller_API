from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from .views import TranscribeAudioView, DiscursoListaView, DiscursoloDetalleView

urlpatterns = [
    #path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title="UsuarioAPI")),
    path('transcribe-audio/', TranscribeAudioView.as_view(), name='transcribe_audio'),
    path('discurso/', DiscursoListaView.as_view()),
    path('discurso/<int:pk>/', DiscursoloDetalleView.as_view()),

]   
