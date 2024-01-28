import os
from dotenv import load_dotenv
load_dotenv()


class SupabaseConfig:
    def __init__(self) -> None:
        self.__api_url: str = os.getenv('API_URL')
        self.__key: str = os.getenv('SUPABASE_KEY')

        assert self.__api_url is not None, "API URL not found."
        assert self.__key is not None, "Supabase key not found."

    def get_api_url(self) -> str:
        return self.__api_url

    def get_key(self) -> str:
        return self.__key
