from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from .views import * 
from ..retroalimentacion.views import RetroalimentacionListCreateView,RetroalimentacionDetailView
from .views import ListaDiscursosUsuario
#from apps.retroalimentacion import views as retroalimentacion_views  # Importa las vistas de retroalimentación

#retroalimentacion_view

urlpatterns = [
    #path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title="Documentation API")),
    path('transcribe-audio/', TranscribeAudioView.as_view(), name='transcribe_audio'),
    path('discurso/', DiscursoListaView.as_view()),
    path('discurso/<int:pk>/', DiscursoloDetalleView.as_view()),
    path('retroalimentacion/generate/<int:discurso_id>/', retroalimentacion_view, name='retroalimentacion'),
    path('retroalimentacion/', RetroalimentacionListCreateView.as_view(), name='retroalimentacion-list'),
    path('retroalimentacion/<int:pk>/', RetroalimentacionDetailView.as_view(), name='retroalimentacion-detail'),
    path('usuario/<str:uid>/', ListaDiscursosUsuario.as_view(), name='lista_discursos_usuario'),
    path('usuario/<str:uid>/<int:id_discurso>/', DetalleDiscurso.as_view(), name='detalle_discurso'),

]


 
