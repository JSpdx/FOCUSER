from django.shortcuts import render

def home(request):
    return render(request, 'Focuser/focuser_home.html')

