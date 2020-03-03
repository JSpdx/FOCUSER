from django.shortcuts import render

# Create your views here.
def vinyl_collection_home(request):
    return render(request, 'VinylCollection/VinylCollection_Home.html')