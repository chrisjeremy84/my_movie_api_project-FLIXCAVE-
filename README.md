# my_movie_api_project-FLIXCAVE-

<img src="https://user-images.githubusercontent.com/53315778/126880784-eb041e0b-1570-4374-bfcb-bca3f4d21ba3.png" height=360 width=580/>

## Table of contents
* [Introduction](#Introduction)
* [Objective](Objective)
* [Technologies](#technologies)
* [Additonal_Info](Additional_Info)
* [Setup](#setup)

## Introduction
This project is known as FLIXCAVE, and is an applications for movie fans that like to share or recieve recommendations based on the likes and watched.
A project like this is highly recommended, as it brings use of all the necessary fields of knowledge and skills in the course of web develpment.
In this readme you will hopefully find all the information that you need.
The repository is open to look through for any lines necessary for the development of you project. ;)

## Objective
The objective of this project is use all user data to return a detailed course of all movie watched and their taste according to the algorithm ran by the applications,
all this can be made possible by the following technologies

## Technologies
Project is created with:
* Python version: 3.8.5
* Django version: 3.1.4
* Tailwind version: 2.0
* Pytorch version: 1.8.0

## Additional Info
Included in this project is tailwind css, which must be installed through a specific path. Here is a method I use for installing tailwindcss in my django projects, the url is below;
>> https://medium.com/@lendinez/how-to-use-tailwind-in-django-and-not-die-in-the-attempt-2853eb164aa7
Here is also a view of my "INSTALLED_APPS" in my settings.py of my prject folder, it should be the same for you 
| >> INSTALLED_APPS = [
    'Feed.apps.FeedConfig',
    'users.apps.UsersConfig',
      "crispy_forms",
    "crispy_tailwind",
    'django.contrib.admin',
   'django.contrib.auth',
   'django.contrib.contenttypes',
   'django.contrib.sessions',
   'django.contrib.messages',
   'django.contrib.staticfiles',
 ]

## Setup
fork the project ...

```
$ cd /flixcave
$ python manage.py runserver

##ENJOY :-)
-Chris

```
