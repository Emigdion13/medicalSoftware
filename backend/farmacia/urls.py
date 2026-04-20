"""
URLs de la aplicación farmacia.
"""

from django.urls import path
from . import views

app_name = 'farmacia'

urlpatterns = [
    # URLs para Medicamentos (Catálogo)
    path('medicamentos/', views.MedicamentoListView.as_view(), name='medicamento_lista'),
    path('medicamentos/<int:pk>/', views.MedicamentoDetailView.as_view(), name='medicamento_detalle'),
    path('medicamentos/nuevo/', views.MedicamentoCreateView.as_view(), name='medicamento_nuevo'),
    path('medicamentos/<int:pk>/editar/', views.MedicamentoUpdateView.as_view(), name='medicamento_editar'),
    path('medicamentos/<int:pk>/eliminar/', views.MedicamentoDeleteView.as_view(), name='medicamento_eliminar'),

    # URLs para Inventario Farmacia
    path('inventario/', views.InventarioListView.as_view(), name='inventario_lista'),
    path('inventario/<int:pk>/', views.InventarioDetailView.as_view(), name='inventario_detalle'),
    path('inventario/nuevo/', views.InventarioCreateView.as_view(), name='inventario_nuevo'),
    path('inventario/<int:pk>/editar/', views.InventarioUpdateView.as_view(), name='inventario_editar'),
    path('inventario/<int:pk>/eliminar/', views.InventarioDeleteView.as_view(), name='inventario_eliminar'),

    # URLs para Dispensación de Medicamentos
    path('dispensacion/', views.DispensacionListView.as_view(), name='dispensacion_lista'),
    path('dispensacion/nueva/', views.DispensacionCreateView.as_view(), name='dispensacion_nueva'),

    # ── API URLs (new) ───────────────────────────────────────────────
    path('api/medicamentos/', views.api_medicamentos, name='api_medicamentos'),
    path('api/medicamentos/<int:pk>/', views.api_medicamento_detalle, name='api_medicamento_detalle'),
    path('api/medicamentos/create/', views.api_medicamento_create, name='api_medicamento_create'),
    path('api/medicamentos/<int:pk>/update/', views.api_medicamento_actualizar, name='api_medicamento_update'),
    path('api/medicamentos/<int:pk>/delete/', views.api_medicamento_eliminar, name='api_medicamento_delete'),
    path('api/inventario/', views.api_inventario, name='api_inventario'),
    path('api/inventario/create/', views.api_inventario_create, name='api_inventario_create'),
    path('api/inventario/<int:pk>/update/', views.api_inventario_actualizar, name='api_inventario_update'),
    path('api/inventario/<int:pk>/delete/', views.api_inventario_eliminar, name='api_inventario_delete'),
    path('api/registros/', views.api_registros, name='api_registros'),
    path('api/registros/<int:pk>/', views.api_registro_detalle, name='api_registro_detalle'),
    path('api/registros/create/', views.api_registro_create, name='api_registro_create'),
    path('api/registros/<int:pk>/update/', views.api_registro_actualizar, name='api_registro_update'),
    path('api/registros/<int:pk>/delete/', views.api_registro_eliminar, name='api_registro_delete'),
    path('api/recetas/', views.api_recetas, name='api_recetas'),
    path('api/recetas/<int:pk>/', views.api_receta_detalle, name='api_receta_detalle'),
    path('api/recetas/create/', views.api_receta_create, name='api_receta_create'),
    path('api/recetas/<int:pk>/update/', views.api_receta_actualizar, name='api_receta_update'),
    path('api/recetas/<int:pk>/delete/', views.api_receta_eliminar, name='api_receta_delete'),
    path('api/dispensaciones/', views.api_dispensaciones, name='api_dispensaciones'),
    path('api/dispensaciones/<int:pk>/', views.api_dispensacion_detalle, name='api_dispensacion_detalle'),
    path('api/dispensaciones/create/', views.api_dispensacion_create, name='api_dispensacion_create'),
    path('api/dispensaciones/<int:pk>/update/', views.api_dispensacion_actualizar, name='api_dispensacion_update'),
    path('api/dispensaciones/<int:pk>/delete/', views.api_dispensacion_eliminar, name='api_dispensacion_delete'),
]
