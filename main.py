"""
Purpose: This module is responsible for running the Flask web server.
"""

# Import the function create_app from the website module.
# This function is typically responsible for setting up the Flask application,
# including registering blueprints, initializing extensions, and loading configuration.
from website import create_app

# Call the create_app function to create an instance of the Flask application.
# This instance is often referred to as the "app", and it's the central object of any Flask application.
app = create_app()

# This conditional is used to check whether this module is being run directly.
# If it is, then the Flask development server is started.
if __name__ == '__main__': 
    
    # Run the Flask development server.
    # The debug parameter is set to True, so the server will provide detailed error messages,
    # and it will automatically reload the application whenever a change is detected in the source code.
    app.run(debug=True)
