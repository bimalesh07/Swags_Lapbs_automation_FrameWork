import os
from dotenv import load_dotenv
current_file = os.path.abspath(__file__)                           # Utilities/ReadEnv.py
project_root = os.path.dirname(os.path.dirname(current_file))       # Main Framework Root
env_path = os.path.join(project_root, '.env')
#load the path
load_dotenv(dotenv_path=env_path)


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
    
    @staticmethod
    def get_username():   
        return os.getenv("LOGIN_USER_API")
    
    @staticmethod
    def get_password(): 
        return os.getenv("API_PASSWORD")