import os
from dotenv import load_dotenv
load_dotenv()


class DiscordConfig:
    def __init__(self) -> None:
        self.__token: str = os.getenv('DISCORD_TOKEN')
        self.__guild_id: int = int(os.getenv('DISCORD_GUILD'))
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

        assert self.__token is not None, "Token not found."
        assert self.__guild_id is not None, "Guild ID not found."

    def get_token(self) -> str:
        return self.__token

    def get_guild_id(self) -> int:
        return self.__guild_id

    def get_commands_info(self) -> list[dict]:
        return self.__commands_info
