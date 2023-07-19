"""
Purpose: Makes the current directory a Python package and when imported this contents of this file will be automatically executed
"""

from flask import Flask

def create_app(): 

    # Initialize the flask application
    app = Flask(__name__)

    # In production you would never want to make this public
    # Encrypt the cookies and session data related to the website
    app.config['SECRET_KEY'] = 'fjfhdskajfhdjkfsdjkhfjsd'

    from .views import views
    from .auth import auth

    # Register the blueprints with the Flask application 
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app