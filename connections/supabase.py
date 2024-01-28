from supabase import create_client, Client


class SupabaseInstance:
    def __init__(self, api_url: str, supabase_key: str) -> None:
        self.__api_url = api_url
        self.__supabase_key = supabase_key

    def get_instance(self) -> Client:
        return create_client(self.__api_url, self.__supabase_key)
