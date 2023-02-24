import discord
from discord import app_commands
from typing import Literal
import config
from botFunctionality import *

def main():
    client = MyClient(config.guildId)
    gSheet = Sheet.getSheetState()
    embedFactory = Embeds()
    
    @client.tree.command(description="Get all data")
    async def getall(interaction: discord.Interaction):
        try:
            data = gSheet.getAllData()
            await interaction.response.send_message('Received data. ✅', ephemeral=True, delete_after=5)
            title, currentPage, currentIndex, itemsPerPage ="All Problems", 1, 0, 5
            pagination = DefaultView(gSheet, embedFactory, data, title, currentPage, currentIndex, itemsPerPage)
            embed = embedFactory.createEmbed(data, title, currentPage, currentIndex, itemsPerPage)
            message = await interaction.channel.send(embed=embed, view=pagination)
            await pagination.wait()
            await message.delete()
        except:
            await interaction.response.send_message('Could not send spreadsheet data ❌', ephemeral=True)
    
    @client.tree.command(description="Filter data by category")
    @app_commands.describe(category="Problem category")
    async def getcategory(interaction: discord.Interaction, category: Literal['Arrays', '2-Pointer', 'Stack', 'Binary Search', 'Sliding Window', 'Linked List', 'Trees', 'Tries', 'Heap', 'Intervals', 'Greedy', 'Backtracking', 'Graphs', '1D-DP', '2D-DP', 'Bit Manipulation', 'Math']):
        try:
            data = gSheet.filterByCategory(category)

            if not data:
                await interaction.response.send_message('There are no entries with this category.' , ephemeral=True, delete_after=10)
                return
            await interaction.response.send_message('Received data. ✅', ephemeral=True, delete_after=5)
            
            currentPage, currentIndex, itemsPerPage = 1, 0, 5
            pagination = DefaultView(gSheet, embedFactory, data, category, currentPage, currentIndex, itemsPerPage)
            embed = embedFactory.createEmbed(data, category, currentPage, currentIndex, itemsPerPage)
            message = await interaction.channel.send(embed=embed, view=pagination)
            await pagination.wait()
            await message.delete()
        except:
            await interaction.response.send_message('Could not send spreadsheet data ❌', ephemeral=True)

    @client.tree.command(description="Create new leetcode entry")
    async def newentry(interaction: discord.Interaction):
        await interaction.response.send_modal(LeetcodeEntry())

    client.run(config.token)

if __name__ == "__main__":
    main()