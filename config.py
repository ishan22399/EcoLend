# Contents of /EcoLend/EcoLend/config.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///site.db'
    DEBUG = os.environ.get('DEBUG') or True
    # Add other configuration variables as needed