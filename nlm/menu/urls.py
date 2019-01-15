from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('json_menu/', views.json_menu),
	path('dash/', views.dash),
	path('advanced/', views.advanced),
	path('scrape_results/', views.scrape_results),
]