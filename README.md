# AWARDS.

An application that will allow a user to post a project he/she has created and get it reviewed by his/her peers.

## Getting Started.

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

* $ git clone https://github.com/annstella/Awards/
* $ cd awards
* $ source virtual/bin/activate

Install all the necessary requirements by running pip install -r requirements.txt (Python 3.6).
* $ configure your prefered database provider in the settings.
* $ ./manager.py check
* $ ./manager.py makemigrations Task
* $ ./manager.py migrate
* $./manager.py runserver

### As a user of the application I should be able to:

* View posted projects and their details.
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page.




#### Things you need to install to the software.
* Django==1.11
* django-bootstrap3==11.0.0
* Pillow==5.2.0
* psycopg2==2.7.5
* pytz==2018.5

##### Deployment

Link to a live site:https://awardsteel.herokuapp.com/



#### Known bugs
* ..

#### Authors

Annstella Kagai

#### License

MIT LICENSE (c) 2018,Annstella kagai

#### Acknowledgments
Inspiration