from supabase import create_client, Client


class SupabaseInstance:
    def __init__(self, api_url: str, supabase_key: str) -> None:
        self.__api_url = api_url
        self.__supabase_key = supabase_key
        self.__client = create_client(self.__api_url, self.__supabase_key)
        self.column_map = {
            'UH ID': 'uh_id',
            'yes': True,
            'no': False,
        }

    def update_member_attendees_db(self, data: list[dict], event_id: int, unique_sheet_id: str) -> None:
        self.__client.table('parsedsheets').insert(
            {'id', unique_sheet_id}).execute()

        n_coins = self.__client.table(
            'events').select('n_coins').eq('id', event_id).execute()

        member_ids = []

        for row in data:
            if self.column_map[row['Member'].lower()]:
                member_ids.append(row["UH ID"])

        self.__client.rpc('add_coins_to_members', {
                          'ids': member_ids, 'coins': n_coins}).execute()
