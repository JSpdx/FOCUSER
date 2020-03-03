from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.vinyl_collection_home, name='vinyl'),
    ]