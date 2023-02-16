import discord
from discord import app_commands
from discord.ext import commands, tasks
from typing import Literal
import config
import functionality

def main():
    client = functionality.MyClient.getClientState()
    gs = functionality.GSheet.getGSheetState()
    embedFactory = functionality.Embeds()

    @client.tree.command(name="addnumbers", description="add two numbers")
    # @app_commands.rename(first="1st")
    @app_commands.describe(first="First number", second="Second number")
    # @app_commands.choices(first=[app_commands.Choice(name="one", value=1), app_commands.Choice(name="two", value=2)])
    async def add(interaction: discord.Interaction, first:int, second:int):
        print(gs.leetcodeSheet.sheet1.get_all_records())
        await interaction.response.send_message(f'{first} + {second} = {first + second}')

    @client.tree.command(description="Returns all data from spreadsheet")
    async def all(interaction: discord.Interaction):        
        try:
            data = gs.getAllData()
            # print(data)
            await interaction.response.send_message(embed=embedFactory.createEmbed(data), ephemeral=True)
        except:
            await interaction.response.send_message('Could not send spreadsheet data ❌', ephemeral=True)
    
    # @app_commands.rename(first="1st")
    # @app_commands.choices(first=[app_commands.Choice(name="one", value=1), app_commands.Choice(name="two", value=2)])
    @client.tree.command(description="Filter data by category")
    @app_commands.describe(category="Problem category")
    async def category(interaction: discord.Interaction, category: Literal['Arrays', '2 Pointer', 'Stack', 'Binary Search', 'Sliding Window', 'Linked List', 'Trees', 'Tries', 'Heap', 'Intervals', 'Greedy', 'Backtracking', 'Graphs', '1D DP', '2D DP', 'Bit Manipulation', 'Math']):
        try:
            data = gs.filterByCategory(category)
            print(data)
            embed = embedFactory.createCategoryEmbed(category, data)
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            await interaction.response.send_message('Could not send spreadsheet data ❌', ephemeral=True)

    client.run(config.token)

if __name__ == "__main__":
    main()
