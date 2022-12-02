from . import views
from django.urls import path

urlpatterns = [
   path('', views.index, name='home'),
   path("train", views.train_page, name='train'),
   path("station", views.station_page, name='station'),
   path("path", views.path_page, name='path'),
]