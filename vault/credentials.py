import os
from dotenv import load_dotenv
from os.path import join, dirname

class Credentials():
    
    def __init__(self):
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)

    def get_discord_token(self):
        return os.getenv('DISCORD_TOKEN')
    
    def get_google_api_key(self):
        return os.getenv('GOOGLE_SEARCH_API_KEY')

    def get_google_cse_key(self):
        return os.getenv('GOOGLE_CSE_ID')

    def get_db_config(self):
        return {'user':os.getenv('DB_USER'),'password':os.getenv('DB_PASSWORD'),'host':os.getenv('DB_HOST'),'database':os.getenv('DB_NAME'),'sslmode':'allow','port':os.getenv('DB_PORT')}
