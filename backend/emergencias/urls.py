"""
URLs de la aplicación emergencias.
"""

from django.urls import path
from . import views

app_name = 'emergencias'

urlpatterns = [
    path('', views.EmergenciaListView.as_view(), name='lista'),
    path('<int:pk>/', views.EmergenciaDetailView.as_view(), name='detalle'),
    path('nueva/', views.EmergenciaCreateView.as_view(), name='nueva'),
    path('<int:pk>/editar/', views.EmergenciaUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', views.EmergenciaDeleteView.as_view(), name='eliminar'),
    
    # ── API URLs (new) ───────────────────────────────────────────
    path('api/emergencias/', views.api_emergencias, name='api_emergencias'),
    path('api/emergencias/<int:pk>/', views.api_emergencia_detalle, name='api_emergencia_detalle'),
    path('api/emergencias/create/', views.api_emergencia_create, name='api_emergencia_create'),
    path('api/emergencias/<int:pk>/update/', views.api_emergencia_actualizar, name='api_emergencia_update'),
    path('api/emergencias/<int:pk>/delete/', views.api_emergencia_eliminar, name='api_emergencia_delete'),
]
