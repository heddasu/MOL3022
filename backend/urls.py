"""from django.urls import path
from . import views

urlpatterns = [
    # path('', views.get_pfm, name = "get_pfm"),
    # path('pfm/<int:id>/', views.pfm_detail, name="pfm_detail"),
    path('matrix/', views.get_matrix, name = "get_matrix"),
    path('matrix/<str:matrix_id>/', views.matrix_detail, name="matrix_detail")
]"""


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'matrix', views.MatrixViewSet)
router.register(r'pfm', views.PfmViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls))
]
