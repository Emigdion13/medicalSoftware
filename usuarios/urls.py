"""
URLs de la aplicación usuarios.
"""

from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.UsuarioListView.as_view(), name='lista'),
    path('<int:pk>/', views.UsuarioDetailView.as_view(), name='detalle'),
    path('nuevo/', views.UsuarioCreateView.as_view(), name='nuevo'),
    path('<int:pk>/editar/', views.UsuarioUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', views.UsuarioDeleteView.as_view(), name='eliminar'),
]
