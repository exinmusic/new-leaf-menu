from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('json_menu/', views.json_menu),
]