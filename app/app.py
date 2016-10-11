import os
from flask import Flask, render_template_string
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter
from time import sleep

# Use a Class-based config to avoid needing a 2nd file
# os.getenv() enables configuration through OS environment variables
class ConfigClass(object):
    # Flask settings
    SECRET_KEY =              os.getenv('SECRET_KEY',       'THIS IS AN INSECURE SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',     'sqlite:///basic_app.sqlite')
    CSRF_ENABLED = True

    # Flask-Mail settings
    
    MAIL_USERNAME =           os.getenv('MAIL_USERNAME'       )
    MAIL_PASSWORD =           os.getenv('MAIL_PASSWORD'       )
    MAIL_DEFAULT_SENDER =     os.getenv('MAIL_DEFAULT_SENDER' )
    MAIL_SERVER =             os.getenv('MAIL_SERVER'         )
    MAIL_PORT =           int(os.getenv('MAIL_PORT'           ))
    MAIL_USE_SSL =        int(os.getenv('MAIL_USE_SSL'        ))

    # Flask-User settings
    USER_APP_NAME        = "AppName"                # Used by email templates


def create_application():
    """ Flask application factory """
    
    # Setup Flask app and app.config
    application = Flask(__name__)
    application.config.from_object(__name__+'.ConfigClass')
    # Initialize Flask extensions
    db = SQLAlchemy(application)                            # Initialize Flask-SQLAlchemy
    mail = Mail(application)                                # Initialize Flask-Mail
    application.config.update(dict(
      PREFERRED_URL_SCHEME = os.getenv('PREFERRED_URL_SCHEME', 'https')
    ))
    # Define the User data model. Make sure to add flask.ext.user UserMixin !!!
    class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)

        # User authentication information
        username = db.Column(db.String(50), nullable=False, unique=True)
        password = db.Column(db.String(255), nullable=False, server_default='')
        reset_password_token = db.Column(db.String(100), nullable=False, server_default='')

        # User email information
        email = db.Column(db.String(255), nullable=False, unique=True)
        confirmed_at = db.Column(db.DateTime())

        # User information
        active = db.Column('is_active', db.Boolean(), nullable=False, server_default='0')
        first_name = db.Column(db.String(100), nullable=False, server_default='')
        last_name = db.Column(db.String(100), nullable=False, server_default='')

    # Create all database tables
    db.create_all()

    # Setup Flask-User
    db_adapter = SQLAlchemyAdapter(db, User)        # Register the User model
    user_manager = UserManager(db_adapter, application)     # Initialize Flask-User

    # The Home page is accessible to anyone
    @application.route('/')
    def home_page():
        return render_template_string("""
            {% extends "base.html" %}
            {% block content %}
                <h2>Home page</h2>
                <p>This page can be accessed by anyone.</p><br/>
                <p><a href={{ url_for('home_page') }}>Home page</a> (anyone)</p>
                <p><a href={{ url_for('members_page') }}>Members page</a> (login required)</p>
            {% endblock %}
            """)

    # The Members page is only accessible to authenticated users
    @application.route('/members')
    @login_required                                 # Use of @login_required decorator
    def members_page():
        return render_template_string("""
            {% extends "base.html" %}
            {% block content %}
                <h2>Members page</h2>
                <p>This page can only be accessed by authenticated users.</p><br/>
                <p><a href={{ url_for('home_page') }}>Home page</a> (anyone)</p>
                <p><a href={{ url_for('members_page') }}>Members page</a> (login required)</p>
            {% endblock %}
            """)

    return application


# Start development web server
application = create_application()
if __name__=='__main__':
    application.run(host='0.0.0.0', port=8000, debug=True)
