from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.vinyl_collection_home, name='vinylhome'),
    path('add', views.album_add_view, name='vinyladd'),
    ]