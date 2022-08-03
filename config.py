import os
from dotenv import load_dotenv
from dotenv import dotenv_values

load_dotenv(dotenv_path='.env.dev')

class Config: 
    DATABASE_URL = os.getenv('DATABASE_URL')
