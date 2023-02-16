import discord
import traceback
import functionality

class LeetcodeEntry(discord.ui.Modal, title="Leetcode Information Entry"):
    # Column Headers ['Number', 'Name', 'Category', 'Solution', 'Link', 'Review']
    numberAndName = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Number and Name (⚠️ Format convention: 1-Reverse Linked List [#-Name])",
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
        label="Category (⚠️ Choose 1 option and follow format convention)",
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
        print(gSheet.getAllData())
        await interaction.response.send_message('Created new entry. ✅')
    
    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Unable to create entry. ❌', ephemeral=True)

        traceback.print_tb(error.__traceback__)