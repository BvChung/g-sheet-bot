import discord
import traceback
from .leetcodeEntry import LeetcodeEntry
from .sheet import Sheet

class NewEntry(LeetcodeEntry):
    def __init__(self, *, title: str = ..., gSheet: Sheet) -> None:
        super().__init__(title=title, gSheet=gSheet)
    
    async def on_submit(self, interaction: discord.Interaction) -> None:
        number, name, difficulty = self._validateInputs()

        if self.gSheet.createEntry([int(number), name, difficulty, str(self.topic), str(self.solution), str(self.link), str(self.review).capitalize()]):
            await interaction.response.send_message('Created new entry. ✅', ephemeral=True, delete_after=15)
        else:
            raise Exception('GSpread API Error. ❌')
    
    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message(f'Could not create new entry. ❌\nIssue: {error}.', ephemeral=True, delete_after=30)

        traceback.print_tb(error.__traceback__)