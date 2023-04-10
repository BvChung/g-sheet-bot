import os
from dotenv import load_dotenv
load_dotenv()

class GoogleSheetsConfig:
    def __init__(self) -> None:
        self.__credentials: str = os.getenv('CREDENTIALS_JSON')
        self.__sheet_name: str = os.getenv("SHEET_NAME")

    def get_credentials(self) -> str:
       return self.__credentials
    
    def get_sheet_name(self) -> str:
        return self.__sheet_name