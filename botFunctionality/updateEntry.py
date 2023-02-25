import discord
import traceback
from .leetcodeEntry import LeetcodeEntry, REVIEW, CATEGORIES
from .sheet import Sheet

class UpdateEntry(LeetcodeEntry):
    def __init__(self, *, title: str, gSheet: Sheet, rowNumber) -> None:
        super().__init__(title=title, gSheet=gSheet)
        self.rowNumber = rowNumber
    
    async def on_submit(self, interaction: discord.Interaction) -> None:
        combinedInput = str(self.numberAndName)

        if combinedInput.find('-') == -1:
            raise Exception('Invalid number + name input => #-Name')
        
        hyphen = combinedInput.find('-')
        number = int(combinedInput[0:hyphen:])
        name = combinedInput[hyphen + 1::]

        if str(self.category) not in CATEGORIES:
            raise Exception('Invalid category input: \nOptions: Arrays, 2-Pointer, Stack, Binary Search, Sliding Window, Linked List, Trees, Tries, Heap, Intervals, Greedy, Backtracking, Graphs, 1D-DP, 2D-DP, Bit Manipulation, Math')

        if str(self.review).lower() not in REVIEW:
            raise Exception('Invalid review input')

        if self.gSheet.updateEntry(self.rowNumber, [[number, name, str(self.category), str(self.solution), str(self.link), str(self.review).lower()]]):
            await interaction.response.send_message(f'Updated problem #{number}. ✅', ephemeral=True, delete_after=15)
        else:
            raise Exception('GSpread API Error: Updating entry needs a 2d array of data [[]].')
    
    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message(f'Could not update entry ❌.\nIssue: {error}.', ephemeral=True, delete_after=30)

        traceback.print_tb(error.__traceback__)