from django.urls import include, path
from . import views

## URL Patterns - the first parameter is the pattern, the second is the method you're calling inside of your view
## Third is the name of the pattern/function.

urlpatterns = [
    path('', views.home, name='focuser'),                      #home page
    path('Eclipses', views.index, name='listEclipses'),        #index of eclipses
    path('AddEvent', views.add_event, name='addEclipses'),     #add new eclipse
    path('<int:pk>/Details', views.details, name='details'),   #view eclipse details
    path('<int:pk>/Edit', views.edit, name='edit'),            #edit eclipses
    path('<int:pk>/Delete', views.delete, name='delete'),      #delete eclipses
]