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
]
