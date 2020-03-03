from django.shortcuts import render

def home(request):
    return render(request, 'focuser_home.html')
