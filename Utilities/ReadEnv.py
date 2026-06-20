import os
from dotenv import load_dotenv
load_dotenv()

class ReadEnvvalue:
    
    @staticmethod
    def get_base_url(): 
        return os.getenv("base_url")
    
    
    @staticmethod
    def get_username():  
        return os.getenv("LOGIN_USER")
    
    @staticmethod
    def get_password(): 
        return os.getenv("password")