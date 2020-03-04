from django.urls import include, path
from . import views

## URL Patterns - the first parameter is the pattern, the second is the method you're calling inside of your view
## Third is the name of the pattern/function.

urlpatterns = [
    path('', views.home, name='plant'),  #home page
    path('create', views.create, name='create'), #create page
    path('index', views.index, name='index'), #index page
    path('details', views.details, name='details'), #details page
    ]