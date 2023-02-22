import discord
import traceback
import functionality

CATEGORIES = ["Arrays", "2-Pointer", "Stack", "Binary Search", "Sliding Window", "Linked List", "Trees", "Tries", "Heap", "Intervals", "Greedy", "Backtracking", "Graphs", "1D-DP", "2D-DP", "Bit Manipulation", "Math"]
REVIEW = ['yes', 'no']

class LeetcodeEntry(discord.ui.Modal, title="Leetcode Information Entry"):
    # Column Headers ['Number', 'Name', 'Category', 'Solution', 'Link', 'Review']
    numberAndName = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Number and Name (⚠️ Format: #-Name)",
        placeholder="Input using ",
        max_length=100
    )

    link = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Link",
        placeholder="Problem link",
        max_length=300
    )

    category = discord.ui.TextInput(
        style=discord.TextStyle.paragraph,
        label="Category (⚠️ Choose 1 option & follow format)",
        placeholder="Problem category",
        default="Arrays, 2-Pointer, Stack, Binary Search, Sliding Window, Linked List, Trees, Tries, Heap, Intervals, Greedy, Backtracking, Graphs, 1D-DP, 2D-DP, Bit Manipulation, Math",
        max_length=200
    )

    solution = discord.ui.TextInput(
        style=discord.TextStyle.paragraph,
        label="Solution",
        placeholder="Your solution",
        max_length=1000
    )

    review = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Review",
        placeholder="Input following format: yes or no",
        max_length=3
    )
        
    async def on_submit(self, interaction: discord.Interaction) -> None:
        gSheet = functionality.Sheet.getSheetState()
        combinedInput = str(self.numberAndName)

        if combinedInput.find('-') == -1:
            raise Exception('Invalid number + name input => #-Name')
        
        hyphen = combinedInput.find('-')
        number = int(combinedInput[0:hyphen:])
        name = combinedInput[hyphen + 1::]

        if str(self.category) not in CATEGORIES:
            raise Exception('Invalid category input')

        if str(self.review).lower() not in REVIEW:
            raise Exception('Invalid review input')

        gSheet.createEntry([number, name, str(self.category), str(self.solution), str(self.link), str(self.review).lower()])
        await interaction.response.send_message('Created new entry. ✅', ephemeral=True)
    
    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message(f'{error}. ❌', ephemeral=True)

        traceback.print_tb(error.__traceback__)