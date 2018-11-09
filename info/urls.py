from django.urls import path
from . import views

urlpatterns = [
    path('', views.info_landing, name='info_landing'),
    path('list/', views.info_list, name='info_list'),
    path('<int:pk>/', views.info_detail, name='info_detail'),
]
