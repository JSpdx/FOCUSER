from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.vinyl_collection_home, name='albumHome'),
    path('add', views.album_add_view, name='albumAdd'),
    path('list/', views.list, name='albumList'),
    path('list/<int:pk>/details/', views.details, name='albumDetails'),
    path('list/<int:pk>/details/<int:pk>/edit/', views.edit, name='albumEdit'),
    ]