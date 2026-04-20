"""
URL configuration for medic_system project.
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from citas.views import (
    api_citas, api_cita_detalle, api_citas_create, 
    api_cita_actualizar, api_cita_eliminar
)
from pacientes.views import (
    api_personal, api_personal_detalle, 
    api_personal_create, api_personal_actualizar, api_personal_eliminar
)
from emergencias.views import (
    api_emergencias, api_emergencia_detalle, 
    api_emergencia_create, api_emergencia_actualizar, api_emergencia_eliminar
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('pacientes/', include('pacientes.urls')),
    path('citas/', include('citas.urls')),
    path('emergencias/', include('emergencias.urls')),
    path('farmacia/', include('farmacia.urls')),
    
    # ── Global API endpoints (new) ────────────────────────────────
    path('api/citas/', api_citas, name='api_citas'),
    path('api/citas/<int:pk>/', api_cita_detalle, name='api_cita_detalle'),
    path('api/citas/create/', api_citas_create, name='api_citas_create'),
    path('api/citas/<int:pk>/update/', api_cita_actualizar, name='api_cita_update'),
    path('api/citas/<int:pk>/delete/', api_cita_eliminar, name='api_cita_delete'),
    path('api/pacientes/', api_personal, name='api_pacientes'),
    path('api/pacientes/<int:pk>/', api_personal_detalle, name='api_paciente_detalle'),
    path('api/pacientes/create/', api_personal_create, name='api_paciente_create'),
    path('api/pacientes/<int:pk>/update/', api_personal_actualizar, name='api_paciente_update'),
    path('api/pacientes/<int:pk>/delete/', api_personal_eliminar, name='api_paciente_delete'),
    path('api/emergencias/', api_emergencias, name='api_emergencias'),
    path('api/emergencias/<int:pk>/', api_emergencia_detalle, name='api_emergencia_detalle'),
    path('api/emergencias/create/', api_emergencia_create, name='api_emergencia_create'),
    path('api/emergencias/<int:pk>/update/', api_emergencia_actualizar, name='api_emergencia_update'),
    path('api/emergencias/<int:pk>/delete/', api_emergencia_eliminar, name='api_emergencia_delete'),
]
