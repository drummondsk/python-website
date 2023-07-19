# Import Blueprint from flask. A Blueprint is a way to organize a group of related views and other code.
from flask import Blueprint

# Define a blueprint named 'auth'. This will be used to group routes related to authentication.
# The first parameter is the blueprint's name, and the second parameter is the module or package where the blueprint is located.
auth = Blueprint('auth', __name__)

# Define a route for the '/login' URL, to be handled by the login() view function.
# When users navigate to this URL, they'll be presented with a login page.
# The '@auth.route' decorator is used to bind a view function to a URL route. 
@auth.route('/login')
def login(): 
    return "<p>Login</p>"

# Define a route for the '/logout' URL, to be handled by the logout() view function.
# When users navigate to this URL, they'll be logged out of the application.
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

# Define a route for the '/sign-up' URL, to be handled by the sign_up() view function.
# When users navigate to this URL, they'll be presented with a sign-up page.
@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"
