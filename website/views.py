"""
Purpose: This module is responsible for defining and handling routes for the application's main views (pages).
"""

# Import Blueprint from flask, a tool for organizing groups of related views and other code.
from flask import Blueprint

# Define a blueprint named 'views'. This will be used to group the main routes of the application.
# The first parameter is the blueprint's name, and the second parameter is the module or package where the blueprint is located.
views = Blueprint('views', __name__)

# Define a route for the '/' URL, which typically represents the homepage of a web application.
# The function home() is the view function, which will be invoked when a user navigates to '/'.
# The '@views.route' decorator is used to bind this view function to the '/' URL route.
@views.route('/')
def home(): 
    # This function returns a simple HTML string for testing purposes.
    # In a fully developed application, you would likely return a full HTML template or a data response.
    return "<h1>Test</h1>"
