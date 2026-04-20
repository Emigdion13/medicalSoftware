from django.urls import path
from . import views

app_name = 'pacientes'

urlpatterns = [
    path('', views.PersonalListView.as_view(), name='lista'),
    path('<int:pk>/', views.PersonalDetailView.as_view(), name='detalle'),
    path('nuevo/', views.PersonalCreateView.as_view(), name='nuevo'),
    path('<int:pk>/editar/', views.PersonalUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', views.PersonalDeleteView.as_view(), name='eliminar'),
]
