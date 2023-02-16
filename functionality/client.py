import discord
from discord import app_commands
import config

class MyClient(discord.Client):
    instance = None

    def __init__(self, guildId:int) -> None:
        super().__init__(intents=discord.Intents.all())

        self.guildId = guildId
        self.leetcodeSheet = None
        self.tree = app_commands.CommandTree(self)

    @staticmethod
    def getClientState():
        if not MyClient.instance:
            MyClient.instance = MyClient(config.guildId)
        return MyClient.instance
            
    async def on_ready(self):
        print(f'{self.user} is live 🚀')
    
    async def setup_hook(self) -> None:
        print('Syncing ⏸️')

        myGuild = discord.Object(id=self.guildId)
        self.tree.copy_global_to(guild=myGuild)
        await self.tree.sync(guild=myGuild)