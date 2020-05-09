import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:13062000@localhost:5432/abc'

# TODO IMPLEMENT DATABASE URL

# Remove console warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
