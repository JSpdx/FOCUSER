import datetime                     #used for passing dates in easy to display format
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone   #used for converting time from UTC to users time zone
import requests                     #necessary for datascraping
from bs4 import BeautifulSoup as BS #necessary for datascraping
from .models import Plant          #import the class of Jersey to be able to use object definition
from .forms import PlantForm       #import the Jersey Form to be able to create and save

# Create your views here.

#View function that renders the home page - no context needed
def home(request):
    return render(request, 'plantPlanner/plant_home.html')


#View function to add a new jersey to the database


def create(request):
    form = PlantForm(request.POST or None)     #Gets the posted form, if one exists
    if form.is_valid():                         #Checks the form for errors, to make sure it's filled in
        form.save()                             #Saves the valid form/jersey to the database
                      #Redirects to the index page, which is named 'footy' in the urls
    else:
        print(form.errors)                      #Prints any errors for the posted form to the terminal
        form = PlantForm()                     #Creates a new blank form
    return render(request, 'plantPlanner/plant_create.html', {'form':form})

#View function that controls the main index page - list of jerseys
def index(request):
    get_plants = Plant.Plants.all()      #Gets all the current jerseys from the database
    context = {'plants': get_plants}      #Creates a dictionary object of all the jerseys for the template
    return render(request, 'plantPlanner/plant_index.html', context)
