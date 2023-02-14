import discord
from discord import app_commands
from discord.ext import commands, tasks
import gspread
import config

# gc = gspread.service_account_from_dict(config.credentials)
# leetcodeSheet = gc.open(config.sheetName)
# print(leetcodeSheet.sheet1.get_all_records())

intents = discord.Intents.default()
intents.message_content = True

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents) -> None:
        super().__init__(intents=intents)

        self.counter = 0
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f'{self.user} is live 🚀')
    
    async def setup_hook(self) -> None:
        # self.my_background_task.start()
        print('background start')
    
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        if message.content == "hello":
            print(f'Message from {message.author}: {message.content}')
            await message.reply("hi", mention_author=True)
    
    @tasks.loop(seconds=10)
    async def my_background_task(self):
        channel = self.get_channel(config.test_channel)
        self.counter += 1
        print(self.counter)
        await channel.send(self.counter)
    
    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()
    
# client = MyClient(intents=intents)
# client.run(config.token)