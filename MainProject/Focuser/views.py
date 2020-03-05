
from .forms import EclipseForm
from .models import Eclipse
from django.shortcuts import render, redirect, get_object_or_404

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
    context = {'eclipses': get_eclipses}  # Creates a dictionary object of all the jerseys for the template
    return render(request, 'Focuser/focuser_index.html', context)

def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Eclipse, pk=pk)
    context = {'eclipse': item}
    return render(request, 'Focuser/focuser_details.html', context)

def edit(request):
    return(render(request, 'Focuser/focuser_edit.html'))