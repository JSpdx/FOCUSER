from bs4 import BeautifulSoup
from .forms import EclipseForm, FavoriteForm
from .models import Eclipse, Favorite
from django.shortcuts import render, redirect, get_object_or_404
import requests

iss_counter = 1

def home(request):
    return render(request, 'Focuser/focuser_home.html')


#View function to add a new eclipse to the database
def add_event(request):
    form = EclipseForm(request.POST or None)     #Gets the posted form, if one exists
    if form.is_valid():                         #Checks the form for errors, to make sure it's filled in
        form.save()                             #Saves the valid form/eclipse to the database
        return redirect('listEclipses')                #Redirects to the index page, which is named 'footy' in the urls
    else:
        print(form.errors)                      #Prints any errors for the posted form to the terminal
        form = EclipseForm()                     #Creates a new blank form
    return render(request, 'Focuser/focuser_create.html', {'form':form})

# View function that controls the main index page - list of jerseys
def index(request):
    get_eclipses = Eclipse.Eclipses.all()  # Gets all the current eclipses from the database
    context = {'eclipses': get_eclipses}  # Creates a dictionary object of all the eclipses for the template
    print (get_eclipses)
    return render(request, 'Focuser/focuser_index.html', context)

def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Eclipse, pk=pk)
    context = {'eclipse': item}
    return render(request, 'Focuser/focuser_details.html', context)

def edit(request, pk):
    pk = int(pk)
    item = get_object_or_404(Eclipse, pk=pk)

    form = EclipseForm(request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():  # Checks the form for errors, to make sure it's filled in
            form.save()  # Saves the valid form/eclipse to the database
            return redirect('listEclipses')  # Redirects to the index page, which is named 'footy' in the urls
        else:
            print(form.errors)  # Prints any errors for the posted form to the terminal
            form = EclipseForm()  # Creates a new blank form

    return render(request, 'Focuser/focuser_edit.html', {'form': form, 'item': item})

def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Eclipse, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('listEclipses')
    else:
        return render(request, 'Focuser/focuser_delete.html', {'item': item})

def apod(request):

    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=4a8sB9S0WoqXO6HstMj15Lgqu5isYYpys0675ygO')
    context = response.json()
    if request.method == 'POST':
        if 'date' in request.POST:                      # this IF statement renders a new page based on the user's input
            user_date = request.POST['date']
            response = requests.get('https://api.nasa.gov/planetary/apod?date={}&api_key=4a8sB9S0WoqXO6HstMj15Lgqu5isYYpys0675ygO'.format(user_date))
            context = response.json()
            return render(request, 'Focuser/focuser_apod.html', context)

        elif 'explanation' in request.POST:             #this ELIF saves the current page to the Favorites model
            form = FavoriteForm(request.POST or None)
            if form.is_valid():
                form.save()

    return render(request, 'Focuser/focuser_apod.html', context)



def iss(request):
    global iss_counter
    page = requests.get('https://blogs.nasa.gov/spacestation/feed/')
    soup = BeautifulSoup(page.content, 'html.parser')
    #tag_list = list(soup.children)                                     # these lines are for parsing html. I used "find and find_all" instead.
    #types = [type(item) for item in list(tag_list)]                    #used to find the BeautifulSoup "Tag" object,
    #body = list(soup.children)[1]                                      #targets the tag object
    if request.method == 'POST':
        if 'prev' in request.POST:
            iss_counter += 1
            title = str(soup.find_all('title')[iss_counter].get_text())
            content = str(soup.find_all('content:encoded')[iss_counter - 1])
            context = {'title': title, 'content': content}
            return render(request, 'Focuser/focuser_iss.html', context)

        else:
            iss_counter -= 1
            print(iss_counter)
            title = str(soup.find_all('title')[iss_counter].get_text())
            content = str(soup.find_all('content:encoded')[iss_counter - 1])
            context = {'title': title, 'content': content}
            return render(request, 'Focuser/focuser_iss.html', context)

    title = str(soup.find_all('title')[1].get_text())  # extracts the headline
    content = str(soup.find_all('content:encoded')[0])  # extracts the page's content
    context = {'title': title, 'content': content}
    iss_counter = 1
    return render(request, 'Focuser/focuser_iss.html', context)

def favorites(request):
    get_favorites = Favorite.Favorites.all()
    print(get_favorites)
    context = {'favorite': get_favorites}
    print(context)
    return render(request, 'Focuser/focuser_favorites.html', context)

def display_favorite(request, pk):
    pk = int(pk)
    item = get_object_or_404(Favorite, pk=pk)
    context = {'favorite': item}
    return render(request, 'Focuser/focuser_display_favorite.html', context)

def meteorshower(request):
    response = requests.get('http://api.wolframalpha.com/v1/simple?appid=DEMO&i=What+airplanes+are+flying+overhead%3F')
    context = response
    print (response)
    return render(request, 'Focuser/focuser_meteor_shower.html')

