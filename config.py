import os


class Config:
    DEBUG = True
    SECRET_KEY = 'your_secret_key_here'

    # Database settings
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Pagination settings
    PATIENTS_PER_PAGE = 10  # Number of patients to display per page
    DOCTORS_PER_PAGE = 10  # Number of doctors to display per page
