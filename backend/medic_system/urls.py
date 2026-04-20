"""
URL configuration for medic_system project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('pacientes/', include('pacientes.urls')),
    path('citas/', include('citas.urls')),
    path('emergencias/', include('emergencias.urls')),
    path('farmacia/', include('farmacia.urls')),
]
