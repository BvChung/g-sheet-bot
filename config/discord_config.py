import os
from dotenv import load_dotenv
load_dotenv()

class DiscordConfig:
    def __init__(self) -> None:
        self.__token: str = os.getenv('TOKEN')
        self.__guildId: int = int(os.getenv('MY_GUILD'))
        self.__commands_info: list[dict] = [
        {
            'name': '/getall',
            'description': 'Returns all spreadsheet data.'
        }, 
        {
            'name': '/getcategory',
            'description': 'Filters and returns all spreadsheet data based on category.'
        }, 
        {
            'name': '/newentry',
            'description': 'Create new leetcode entry.'
        }, 
        {
            'name': '/updateentry',
            'description': 'Update leetcode entry based on problem number inputted.'
        }, 
        {
            'name': '/deleteentry',
            'description': 'Delete leetcode entry based on problem number inputted.'
        },
        ]
    
    def get_token(self) -> str:
        return self.__token
    
    def get_guild_id(self) -> int:
        return self.__guildId
    
    def get_commands_info(self) -> list[dict]:
        return self.__commands_info