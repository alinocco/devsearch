# Devsearch

The platform for programmers to share their projects. 

## Table of contents
* [Live Demo](#live-demo)
* [General Info](#general-info)
* [Functionality](#functionality)
* [Technologies](#technologies)
* [Setup](#setup)
* [Resources](#resources)

## Live Demo
https://alinocco-devsearch.herokuapp.com

## General Info
The users can
1. Share their projects
2. Give feedback on others' works
3. Contact to each other
4. Search for projects/programmers
    
## Functionality
* Basic Django Overview
* Database Design and Models
* CRUD
* Static Files
* Connect Frontend Files and UIkit
* User Registration & Authentification
* Search
* Pagination
* Send a Welcome Email 
* Reset Password via Email
* API on Django Rest Framework
* Deployment

## Plans
* Forum based on [Python Django 7 Hour Course by Dennis Ivy](https://youtu.be/PtQiiknWUcI)
* Video Streaming Room based on [Building A Video Chat Application by Dennis Ivy](https://youtu.be/1cYKoSe3MN4)
    
## Technologies
The project is written on **Python: 3.8/Django: 4.0** with implementation of:
* **Poetry: 1.1.12** - virtual environment and dependencies' manager
* **Pillow: 9.1.1** - Python library for processing images
* **Whitenoise: 6.2.0** - Serve our static files
* **Django-Cleanup: 6.0.0** - Remove unused images, files etc.
* **Django Rest Framework: 3.13.1** - Bulding REST API
* **Django Rest Framework Simple JWT: 5.2.0** - JSON Web Tokens
* **Django CORS Headers: 3.13.0** - Resolving Cross-origin resource sharing
* **Django-environ: 0.9.0** - Hide environment variables in .env
* **Psycopg2: 2.9.3** - Connect our app to PosgreSQL Database
* **Gunicorn: 20.1.0** - Deploy on server
* **Django-heroku: 0.3.1** - Deploy on Heroku

## Setup
1. Clone the repository by
   ```
   git clone https://github.com/alinocco/devsearch.git
   ```
2. Go to project folder
   ```
   cd devsearch
   ```
3. Install **poetry**
   ```
   pip install poetry
   ```
4. Activate virtual environment
   ```
   poetry shell
   ```
5. Migrate all project migrations
   ```
   python manage.py migrate
   ```
6. Run project
   ```
   python manage.py runserver
   ```
   
## Resources
The project is done following [**Full Django Course by Dennis Ivy**](https://www.udemy.com/course/python-django-2021-complete-course/) with some new changes and features.

Updates:
* poetry instead of virtualenv
* work with Git and Github
* troubleshoot issues with error messages

While watching the lectures, I was taking [notes](https://docs.google.com/document/d/10IwWR-TRoy1c1zjYlUVPUaUgIQkxy2mqUJnwSmlAQ10/edit#)(click to follow).
