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
	
	
	- Used the MVC/MTV framework Django to build a web application in the Python 
	- Integrated APIs from NASA and Wolfram Alpha to add dynamic, self-updating features to the application
	- USED HTML GET and POST methods to add state to pages.
	- Used SQLite RDBMS to store form entries, and user selected favorites 
	- Used Virtualenv virtual environment to maintain a consistent and compatible development environment
	- Used Agile methodologies throughout development including daily standups and user stories to keep production moving forward
	- Used Azure DevOps as a platform for project management
	- Used Git to maintain code integrity in a team with multiple developers
	
- Languages used:
	- Python
	- Javascript
	- HTML and CSS

This project proved to be a great learning opportunity for me. Working on a project with multiple people gave me some good experience utilizing version control, 
and successfully merging conflicts. Learning to use an MVC like Django (technically MTV) was very beneficial too. I have since been exposed to other MVC framworks such as React, and the learning curve
was greatly reduced. I learned


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

				
