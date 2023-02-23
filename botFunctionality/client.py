import discord
from discord import app_commands

class MyClient(discord.Client):
    def __init__(self, guildId:int) -> None:
        super().__init__(intents=discord.Intents.all())

        self.guildId = guildId
        self.leetcodeSheet = None
        self.tree = app_commands.CommandTree(self)
            
    async def on_ready(self) -> None:
        print(f'{self.user} is live 🚀')
    
    async def setup_hook(self) -> None:
        print('Syncing 🔃')

        myGuild = discord.Object(id=self.guildId)
        self.tree.copy_global_to(guild=myGuild)
        await self.tree.sync(guild=myGuild)