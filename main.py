import discord
from discord import app_commands
from typing import Literal
import config
from functionality import *

def main():
    client = MyClient.getClientState()
    gSheet = Sheet.getSheetState()
    embedFactory = Embeds()

    # @client.tree.command(description="Returns all data from spreadsheet")
    # async def all(interaction: discord.Interaction):        
    #     try:
    #         data = gSheet.getAllData()
    #         # print(data)
    #         embed = embedFactory.defaultEmbed(data)
    #         await interaction.response.send_message(embed=embed, ephemeral=True)
    #     except:
    #         await interaction.response.send_message('Could not send spreadsheet data ❌', ephemeral=True)
    
    @client.tree.command(description="Filter data by category")
    @app_commands.describe(category="Problem category")
    async def category(interaction: discord.Interaction, category: Literal['Arrays', '2-Pointer', 'Stack', 'Binary Search', 'Sliding Window', 'Linked List', 'Trees', 'Tries', 'Heap', 'Intervals', 'Greedy', 'Backtracking', 'Graphs', '1D-DP', '2D-DP', 'Bit Manipulation', 'Math']):
        try:
            data = gSheet.filterByCategory(category)
            
            if not data:
                await interaction.response.send_message('There are no entries with this category.')
                return

            embed = embedFactory.categoryEmbed(category, data)
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            await interaction.response.send_message('Could not send spreadsheet data ❌', ephemeral=True)

    @client.tree.command(description="Create new leetcode entry")
    @app_commands.describe()
    async def sort(interaction: discord.Interaction):
        gSheet.sortSheet()
        await interaction.response.send_message('Sorted', ephemeral=True)

    @client.tree.command(description="Create new leetcode entry")
    async def entry(interaction: discord.Interaction):
        # interaction.response.
        await interaction.response.send_modal(LeetcodeEntry())

    @client.tree.command(description="test view")
    async def getall(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        data = gSheet.getAllData()
        currentPage = 1
        currentIndex = 0
        itemsPerPage = 5
        pagination = PaginatedView(embedFactory, data, currentPage, currentIndex, itemsPerPage)
        embed = embedFactory.paginatedEmbed(data, currentPage, currentIndex, itemsPerPage)
        message = await interaction.channel.send(embed=embed, view=pagination)
        await pagination.wait()
        # print(f'Counter {pagination.counter}')
        await message.delete()
    
    client.run(config.token)

if __name__ == "__main__":
    main()
