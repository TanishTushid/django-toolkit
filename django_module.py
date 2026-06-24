"""
django.shortcuts

This module provides helper functions that make it easier to work with
views in Django.

- render()   : Combines a template with data (context) and returns an
               HttpResponse object.
- redirect() : Redirects the user to another URL, view, or route.
"""
from django.shortcuts import render, redirect


"""
django.http

This module contains classes used for handling HTTP requests and responses.

- HttpResponse : Used to send a custom response back to the browser.
                 Example: returning plain text, HTML, JSON, etc.
"""
from django.http import HttpResponse


"""
.models

Imports models defined in the current application's models.py file.

- Receipe : A database model that represents recipe data.
            Django uses models to create, read, update, and delete
            records from the database.
"""
from .models import Receipe


"""
django.contrib.auth.models

Provides built-in authentication models.

- User : Django's default user model used for storing user information
         such as username, email, password, first name, last name, etc.
"""
from django.contrib.auth.models import User


"""
django.contrib.messages

Django's messaging framework.

Used to display one-time notifications/messages to users.

Examples:
- Success messages
- Error messages
- Warning messages
- Informational messages

Example:
message.success(request, "Recipe added successfully!")
"""
from django.contrib import messages as message


"""
django.contrib.auth

Provides authentication functions for user login and logout.

- authenticate() : Verifies user credentials (username/password).
- login()        : Creates a user session after successful authentication.
- logout()       : Ends the current user session.
"""
from django.contrib.auth import authenticate, login, logout


"""
django.contrib.auth.decorators

Provides decorators related to authentication.

- login_required : Restricts access to a view.
                   Only authenticated users can access the view.
                   Unauthenticated users are redirected to the login page.

Example:

@login_required
def home(request):
    return render(request, 'home.html')
"""
from django.contrib.auth.decorators import login_required


"""
django.db.models

This module contains Django's Object Relational Mapping (ORM) classes.

The ORM allows you to interact with the database using Python code
instead of writing raw SQL queries.

- Model       : Base class for creating database tables.
- CharField   : Stores short text values.
- TextField   : Stores large amounts of text.
- IntegerField: Stores integer numbers.
- DateField   : Stores dates.
- ImageField  : Stores image file paths.
- ForeignKey  : Creates a relationship between two models.
- ManyToManyField : Creates a many-to-many relationship.
- BooleanField: Stores True/False values.

Example:

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='recipes/')
"""
from django.db import models



