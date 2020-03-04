from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import AlbumForm

# Create your views here.
def vinyl_collection_home(request):
    return render(request, 'VinylCollection/VinylCollection_Home.html')

def album_add_view(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = AlbumForm()
    return render(request, "VinylCollection/Album_Add.html", {'form': form})