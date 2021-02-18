from django.urls import path
from . import views

urlpatterns = [
    # path('', views.get_pfm, name = "get_pfm"),
    # path('pfm/<int:id>/', views.pfm_detail, name="pfm_detail"),
    path('matrix/', views.get_matrix, name = "get_matrix"),
    path('matrix/<str:matrix_id>/', views.matrix_detail, name="matrix_detail")
]