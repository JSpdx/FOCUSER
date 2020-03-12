import datetime                     #used for passing dates in easy to display format
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone   #used for converting time from UTC to users time zone
import requests                     #necessary for datascraping
from bs4 import BeautifulSoup as BS #necessary for datascraping
from .models import Plant          #import the class of Plant to be able to use object definition
from .forms import PlantForm       #import the Plant Form to be able to create and save

# Create your views here.

#View function that renders the home page - no context needed
def home(request):
    return render(request, 'plantPlanner/plant_home.html')


#View function to add a new plant to the database


def create(request):
    form = PlantForm(request.POST or None)     #Gets the posted form, if one exists
    if form.is_valid():                         #Checks the form for errors, to make sure it's filled in
        form.save()                             #Saves the valid form to the database

    else:
        print(form.errors)
        form = PlantForm()                     #Creates a new blank form
    return render(request, 'plantPlanner/plant_create.html', {'form':form})

#View function that controls the main index page - list of plants in garden
def index(request):
    get_plants = Plant.Plants.all()      #Gets all the current plants from the database
    context = {'plants': get_plants}      #Creates a dictionary object of all the plants for the template
    return render(request, 'plantPlanner/plant_index.html', context)

#View function to look up the details of a plant
def details_plant(request, pk):
    pk = int(pk)                                #Casts value of pk to an int so it's in the proper form
    plant = get_object_or_404(Plant, pk=pk)   #Gets single instance of the plant from the database
    context={'plant':plant}                   #Creates dictionary object to pass the plant object
    return render(request,'plantPlanner/plant_details.html', context)

def edit(request, pk):
    pk = int(pk)
    item = get_object_or_404(Plant, pk=pk)

    form = PlantForm(request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():  # Checks the form for errors, to make sure it's filled in
            form.save()  # Saves the valid form/eclipse to the database
            return redirect('index')  # Redirects to the index page, which is named 'footy' in the urls
        else:
            print(form.errors)  # Prints any errors for the posted form to the terminal
            form = PlantForm()  # Creates a new blank form

    return render(request, 'plantPlanner/plant_edit.html', {'form': form, 'item': item})

def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Plant, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    else:
        return render(request, 'plantPlanner/plant_delete.html', {'item': item})

def api(request):

    url = 'https://trefle.io/api/plants/?' # url to api to query a plant

    params = {
        'token': 'TnlvTmxtcWY1RkNsb2EwNUZqY0FGUT09',  # access token
        'q': ''  # user's input is set to required parameter
    }
    response = requests.get(url, params=params)
    context = {'response': response.json()}

    if request.method == 'POST':
        if 'flower' in request.POST:
            select_flower = request.POST['flower']  # grabs user input and assigns it to select_flower
            params = {
                'token': 'TnlvTmxtcWY1RkNsb2EwNUZqY0FGUT09',  # access token
                'q': select_flower  # user's input is set to required parameter
            }
            response = requests.get(url, params=params)
            context = { 'response': response.json()  }
            return render(request, 'plantPlanner/plant_api.html', context)

    return render(request, 'plantPlanner/plant_api.html', context)
