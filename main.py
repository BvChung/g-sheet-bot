import discord
from discord import app_commands
from typing import Literal
import config
import functionality

def main():
    client = functionality.MyClient.getClientState()
    gSheet = functionality.Sheet.getSheetState()
    embedFactory = functionality.Embeds()

    @client.tree.command(description="Returns all data from spreadsheet")
    async def all(interaction: discord.Interaction):        
        try:
            data = gSheet.getAllData()
            # print(data)
            await interaction.response.send_message(embed=embedFactory.createEmbed(data), ephemeral=True)
        except:
            await interaction.response.send_message('Could not send spreadsheet data ❌', ephemeral=True)
    
    @client.tree.command(description="Filter data by category")
    @app_commands.describe(category="Problem category")
    async def category(interaction: discord.Interaction, category: Literal['Arrays', '2-Pointer', 'Stack', 'Binary Search', 'Sliding Window', 'Linked List', 'Trees', 'Tries', 'Heap', 'Intervals', 'Greedy', 'Backtracking', 'Graphs', '1D-DP', '2D-DP', 'Bit Manipulation', 'Math']):
        try:
            data = gSheet.filterByCategory(category)
            print(data)
            embed = embedFactory.createCategoryEmbed(category, data)
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            await interaction.response.send_message('Could not send spreadsheet data ❌', ephemeral=True)

    @client.tree.command(description="Create new leetcode entry")
    @app_commands.describe(number="Problem number", name="Problem name", category="Problem category", solution="Your solution", link="Problem link", review="Review problem")
    async def newentry(interaction: discord.Interaction, number:app_commands.Range[int, 0, None], name: str,  category: Literal['Arrays', '2 Pointer', 'Stack', 'Binary Search', 'Sliding Window', 'Linked List', 'Trees', 'Tries', 'Heap', 'Intervals', 'Greedy', 'Backtracking', 'Graphs', '1D DP', '2D DP', 'Bit Manipulation', 'Math'], solution: str, link: str, review: Literal['yes', 'no']):
        try:
            # data = gs.filterByCategory(category)
            # print(data)
            # embed = embedFactory.createCategoryEmbed(category, data)
            await interaction.response.send_message("Success", ephemeral=True)
        except:
            await interaction.response.send_message('Could not send spreadsheet data ❌', ephemeral=True)

    @client.tree.command(description="Create new leetcode entry")
    async def entry(interaction: discord.Interaction):
        await interaction.response.send_modal(functionality.LeetcodeEntry())

    client.run(config.token)

if __name__ == "__main__":
    main()
