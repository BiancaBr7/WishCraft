from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_wish, name='create_wish'),
    path('view_wish/<int:pk>/', views.view_wish, name='view_wish'),
]