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
        # gc = gspread.service_account_from_dict(config.credentials)
        # self.leetcodeSheet = GSheets.getGSheetsState()

        myGuild = discord.Object(id=self.guildId)
        self.tree.copy_global_to(guild=myGuild)
        await self.tree.sync(guild=myGuild)
        # self.my_background_task.start()
    
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        if message.content == "hello":
            print(f'Message from {message.author}: {message.content}')
            await message.reply("hi", mention_author=True)
    
    # @tasks.loop(seconds=10)
    # async def my_background_task(self):
    #     channel = self.get_channel(config.test_channel)
    #     self.counter += 1
    #     print(self.counter)
    #     await channel.send(self.counter)
    
    # @my_background_task.before_loop
    # async def before_my_task(self):
    #     await self.wait_until_ready()
