"""
URLs de la aplicación farmacia.
"""

from django.urls import path
from . import views

app_name = 'farmacia'

urlpatterns = [
    # Rutas para inventario
    path('inventario/', views.InventarioListView.as_view(), name='inventario_lista'),
    path('inventario/<int:pk>/', views.InventarioDetailView.as_view(), name='inventario_detalle'),
    path('inventario/nuevo/', views.InventarioCreateView.as_view(), name='inventario_nuevo'),
    path('inventario/<int:pk>/editar/', views.InventarioUpdateView.as_view(), 
         name='inventario_editar'),
    path('inventario/<int:pk>/eliminar/', views.InventarioDeleteView.as_view(),
         name='inventario_eliminar'),
    
    # Rutas para dispensación
    path('dispensacion/', views.DispensacionListView.as_view(), name='dispensacion_lista'),
    path('dispensacion/nueva/', views.DispensacionCreateView.as_view(), 
         name='dispensacion_nueva'),
]
