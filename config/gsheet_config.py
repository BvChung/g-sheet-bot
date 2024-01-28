import os
from dotenv import load_dotenv
load_dotenv()


class GSheetConfig:
    def __init__(self) -> None:
        self.__credentials_filename: str = os.getenv('CREDENTIALS_JSON')
        self.__spreadsheet_key: str = os.getenv('SPREADSHEET_KEY')

        assert self.__credentials_filename is not None, "Credentials filename not found."
        assert self.__spreadsheet_key is not None, "Spreadsheet key not found."

    def get_credentials_filename(self) -> str:
        return self.__credentials_filename

    def get_spreadsheet_key(self) -> str:
        return self.__spreadsheet_key
