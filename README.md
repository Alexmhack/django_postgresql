# django_postgresql
using postgresql database with django

# INSTALLATION
Install the postgresql database in your local computer first from the .exe file on the offical site.

Install the postgresql package for python - psycopg2 using pip in virtualenv

# CONFIGURE
Create a new virtualenv and then install all the dependencies for our project there

Create a new django project

Create a new database using the postgresql command line.

CREATE DATABASE blog

Inside our django project settings.py, set the database as the postgresql like so,

'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '',
    }

# DJANGO USAGE