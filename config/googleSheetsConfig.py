import os
from dotenv import load_dotenv
load_dotenv()

class GoogleSheetsConfig:
    def __init__(self) -> None:
        self.__credentials: dict = {
            "type": os.getenv('TYPE'),
            "project_id": os.getenv('PROJECT_ID'),
            "private_key_id": os.getenv('PRIVATE_KEY_ID'),
            "private_key": os.getenv('PRIVATE_KEY').replace(r'\n', '\n'),
            "client_email": os.getenv('CLIENT_EMAIL'),
            "client_id": os.getenv('CLIENT_ID'),
            "auth_uri": os.getenv('AUTH_URI'),
            "token_uri": os.getenv('TOKEN_URI'),
            "auth_provider_x509_cert_url": os.getenv('AUTH_PROVIDER_X509_CERT_URL'),
            "client_x509_cert_url": os.getenv('CLIENT_X509_CERT_URL')
            }
        
        self.__sheetName: str = os.getenv("SHEET_NAME")

    def getCredentials(self)->dict:
       return self.__credentials
    
    def getSheetName(self)->str:
        return self.__sheetName