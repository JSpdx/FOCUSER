import datetime                     #used for passing dates in easy to display format
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone   #used for converting time from UTC to users time zone
import requests                     #necessary for datascraping
from bs4 import BeautifulSoup as BS #necessary for datascraping

# Create your views here.

#View function that renders the home page - no context needed
def home(request):
    return render(request, 'plantPlanner/plant_home.html')

