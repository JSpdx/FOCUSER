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

def edit(request, pk):
    pk = int(pk)
    get_album = get_object_or_404(Album, pk=pk)
    form = AlbumForm(request.POST or None, instance=get_album)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('albumList')
        else:
            print(form.erros)
            form = AlbumForm()
    return render(request, 'VinylCollection/Album_Edit.html', {'form': form, 'get_album': get_album})

def delete(request, pk):
    pk = int(pk)
    del_album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        del_album.delete()
        return redirect('albumList')
    else:
        return render(request, 'VinylCollection/Album_Delete.html', {'del_album': del_album})