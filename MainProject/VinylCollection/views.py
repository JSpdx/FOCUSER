from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlbumForm
from .models import Album

# Create your views here.
def vinyl_collection_home(request):
    return render(request, 'VinylCollection/VinylCollection_Home.html')

def album_add_view(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('albumList')
    else:
        form = AlbumForm()
    return render(request, "VinylCollection/Album_Add.html", {'form': form})

def list(request):
    get_albums = Album.Albums.all()
    context = {'Albums': get_albums}
    return render(request, 'VinylCollection/Album_List.html', context)

def details(request, pk):
    pk = int(pk)
    album = get_object_or_404(Album, pk=pk)
    context={'Album':album}
    return render(request,'VinylCollection/Album_Details.html', context)