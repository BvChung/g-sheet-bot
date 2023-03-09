import os
from dotenv import load_dotenv
load_dotenv()

class DiscordConfig:
    def __init__(self) -> None:
        self.__token: str = os.getenv('TOKEN')
        self.__guildId: int = int(os.getenv('MY_GUILD'))
        self.__commandsInfo: list[dict] = [
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
    
    def getToken(self)->str:
        return self.__token
    
    def getGuildId(self)->int:
        return self.__guildId
    
    def getCommandsInfo(self)->list[dict]:
        return self.__commandsInfo