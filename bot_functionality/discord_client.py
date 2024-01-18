import discord
from discord import app_commands


class DiscordClient(discord.Client):
    def __init__(self, guild_id: int) -> None:
        super().__init__(intents=discord.Intents.all())

        self.guild_id = guild_id
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self) -> None:
        print(f'{self.user} is live 🚀')

    async def setup_hook(self) -> None:
        print('Syncing 🔃')

        myGuild = discord.Object(id=self.guild_id)
        self.tree.copy_global_to(guild=myGuild)
        await self.tree.sync(guild=myGuild)
