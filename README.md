# FOCUSER
a web app for displaying astronomy information I built using Django, API's from NASA and Wolfram Alpha, and the webscraping package Beautifulsoup


## Introduction
During a 2 week sprint at the Tech Academy, I used Python and Django to create a web app that displays information for the amateur astronomer, and space nerd.

## Functionality
- Provides a list of upcoming eclipses that can be manually stored, edited and deleted in a SQLite database,
- Displays a picture and description from Nasa's APOD (astronomy picture of the day), 
- Allows users to store their favorite APOD entries in the databse,
- Retrieves information about upcoming meteor showers using Wolfram Alpha's API
- Retrieves information from the International Space Station's RSS feed using the BeautifulSoup webscraping package
	

## Technologies/Practices
- Django MTV/MVC framework 
- Used APIs from NASA and Wolfram Alpha to add dynamic, self-updating features to the application
- Parsed JSON to retrieve the desired information from the API
- Webscraping package BeautifulSoup, used to get data from an RSS
- RESTful architecture, combined HTML GET and POST methods with IF/ELSE statements in Python to add state to pages.
- RDBMS SQLite to store form entries, and user selected favorites 
- Virtualenv virtual environment to maintain a consistent and compatible development environment
- Agile pracices used throughout development including daily standups and user stories to keep production moving forward
- Azure DevOps as a platform for project management
- Git for version control, to maintain code integrity in a team with multiple developers

###Languages used:
- Python
- Javascript
- HTML and CSS

## Highlights

#### Using Django's built in FOR loop tags, I was able to quickly and efficiently create an HTML table that would automatically display all of the eclipse events stored in the database, and reflect an added or subtracted item.

```
	 <table class="table-striped">
            
	    <tr id="column_header">
                <th class="col-md">Date</th>
                <th class="col-md">Locations</th>
                <th class="col-md">Type</th>
                <th class="col-md">Subtype</th>
	    </tr>

            {% for eclipse in eclipses %}     <!-- creates a new row for each eclipse event stored-->
                <tr>
                    <td class="col-md">{{eclipse.date}}</td>
                    <td class="col-md">{{eclipse.locations}}</td>
                    <td class="col-md">{{eclipse.type}}</td>
                    <td class="col-md">{{eclipse.subtype}}</td>

                    <td class="col-md"><a href="{{eclipse.pk}}/Details"><button class="primary-light-button">Details</button></a></td>
                    <td class="col-md"><a href="{{eclipse.pk}}/Edit"><button class="primary-light-button">Edit</button></a></td>
                </tr>
            {% endfor %}
        </table>
```

#### Using Django tags and hidden HTML forms, I was able to pass the API data being displayed on that page to be saved in the DB.

HTML:
```

	<form method ="post">
            {% csrf_token %}
            <input type="hidden" name="title" value="{{title}}">
            <input type="hidden" name="explanation" value="{{explanation}}">
            <input type="hidden" name="image_url" value="{{hdurl}}">
            <button class="btn btn-danger">Save to Favorites</button>
        </form>

```

views.py:
```
 def apod(request):

    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=4a8sB9S0WoqXO6HstMj15Lgqu5isYYpys0675ygO')
    context = response.json()
    if request.method == 'POST':
       
	 if 'date' in request.POST:                      # this IF statement renders a new page based on the user's input
            user_date = request.POST['date']
            response = requests.get('https://api.nasa.gov/planetary/apod?date={}&api_key=4a8sB9S0WoqXO6HstMj15Lgqu5isYYpys0675ygO'.format(user_date))
            context = response.json()
            return render(request, 'Focuser/focuser_apod.html', context)

        elif 'explanation' in request.POST:             # this ELIF saves the current page to the Favorites model
            form = FavoriteForm(request.POST or None)
            if form.is_valid():
                form.save()

    return render(request, 'Focuser/focuser_apod.html', context)
```





This project proved to be a great learning opportunity for me. Working on a project with multiple people gave me some good experience utilizing version control, 
and successfully merging conflicts. Learning to use an MVC like Django (technically MTV) was very beneficial too. I have since been exposed to other MVC frameworks like React, and the learning curve
was greatly reduced.


Working on a legacy codebase was a great learning oppertunity for fixing bugs, cleaning up code, and adding requested features. 
There were some big changes that could have been a large time sink, but we used what we had to deliver what was needed on time. 
I saw how a good developer works with what they have to make a quality product. I worked on several back end stories that I am very proud of. 
Because much of the site had already been built, there were also a good deal of front end stories and UX improvements that needed to be completed, all of varying degrees of difficulty. 
Everyone on the team had a chance to work on front end and back end stories. Over the two week sprint I also had the opportunity to work on some other project management and
team programming skills that I'm confident I will use again and again on future projects.

Below are descriptions of the stories I worked on, along with code snippets and navigation links. I also have some full code files in this repo for the larger functionalities I implemented.












Project needs virtualenv installed in order to run.

1) From environments, run scripts\activate

2) From FOCUSER\mainproject, run python manage.py makemigrations,
			    then python manage.py migrate
			    then python manage.py runserver

This app was written as part of a group project at my bootcamp, and the part I was responsible for was the section called FOCUSER.

				
