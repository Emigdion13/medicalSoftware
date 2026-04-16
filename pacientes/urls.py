"""
URLs de la aplicación pacientes.
"""

from django.urls import path
from . import views

app_name = 'pacientes'

urlpatterns = [
    path('', views.PacienteListView.as_view(), name='lista'),
    path('<int:pk>/', views.PacienteDetailView.as_view(), name='detalle'),
    path('nuevo/', views.PacienteCreateView.as_view(), name='nuevo'),
    path('<int:pk>/editar/', views.PacienteUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', views.PacienteDeleteView.as_view(), name='eliminar'),
]
