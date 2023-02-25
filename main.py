import discord
from discord import app_commands
from typing import Literal
import config
from botFunctionality import *

def main():
    client = MyClient(config.guildId)
    gSheet = Sheet.getState()
    embedFactory = Embeds()
    gSheet.testUpdate()
    
    @client.tree.command(description="Get all data")
    async def getall(interaction: discord.Interaction):
        try:
            if DefaultView.instance:
                return await interaction.response.send_message('There is already an active instance. ⚠️', ephemeral=True, delete_after=15)
                
            data = gSheet.getAllData()
            title, currentPage, currentIndex, itemsPerPage = "All Problems", 1, 0, 5
            pagination = DefaultView.getState(gSheet, embedFactory, data, title, currentPage, currentIndex, itemsPerPage)
            embed = embedFactory.createEmbed(data, title, currentPage, currentIndex, itemsPerPage)
            await interaction.response.send_message('Received data. ✅', ephemeral=True, delete_after=5)
            displayedMessage = await interaction.channel.send(embed=embed, view=pagination)
            await pagination.wait()
            await displayedMessage.delete()
        except:
            await interaction.response.send_message('Could not send spreadsheet data ❌', ephemeral=True, delete_after=30)
    
    @client.tree.command(description="Filter data by category")
    @app_commands.describe(category="Problem category")
    async def getcategory(interaction: discord.Interaction, category: Literal['Arrays', '2-Pointer', 'Stack', 'Binary Search', 'Sliding Window', 'Linked List', 'Trees', 'Tries', 'Heap', 'Intervals', 'Greedy', 'Backtracking', 'Graphs', '1D-DP', '2D-DP', 'Bit Manipulation', 'Math']):
        try:
            if CategoryView.instance:
                return await interaction.response.send_message('There is already an active instance. ⚠️', ephemeral=True, delete_after=15)
                
            data = gSheet.filterByCategory(category)

            if not data:
                return await interaction.response.send_message('There are no entries with this category. ⚠️' , ephemeral=True, delete_after=15)
            
            currentPage, currentIndex, itemsPerPage = 1, 0, 5
            pagination = CategoryView.getState(gSheet, embedFactory, data, category, currentPage, currentIndex, itemsPerPage)
            await interaction.response.send_message('Received data. ✅', ephemeral=True, delete_after=5)
            embed = embedFactory.createEmbed(data, category, currentPage, currentIndex, itemsPerPage)
            displayedMessage = await interaction.channel.send(embed=embed, view=pagination)
            await pagination.wait()
            await displayedMessage.delete()
        except:
            await interaction.response.send_message('Could not send spreadsheet data ❌', ephemeral=True, delete_after=30)

    @client.tree.command(description="Create new entry")
    async def newentry(interaction: discord.Interaction):
        await interaction.response.send_modal(NewEntry(title="New Leetcode Entry", gSheet=gSheet))

    @client.tree.command(description="Update entry")
    @app_commands.describe(number="Problem number")
    async def updateentry(interaction: discord.Interaction, number: int):
        rowInformation = gSheet.getEntry(number)

        if not rowInformation:
            return await interaction.response.send_message(f'Problem #{number} could not be found.', ephemeral=True, delete_after=15)

        rowNumber: int = rowInformation[0]
        rowData: list = rowInformation[1]
        numberAndName = str(rowData[0]) + '-' + rowData[1]
        category = str(rowData[2])
        solution = str(rowData[3])
        link = str(rowData[4])
        review = str(rowData[5])
        
        # Inject current entry's data into modal
        updateModal = UpdateEntry(title=f"Update Entry #{number}", gSheet=gSheet, rowNumber=rowNumber)
        updateModal.numberAndName.default = numberAndName
        updateModal.category.default = category
        updateModal.solution.default = solution
        updateModal.link.default = link
        updateModal.review.default = review

        await interaction.response.send_modal(updateModal)
    
    @client.tree.command(description="Delete entry")
    @app_commands.describe(number="Problem number")
    async def deleteentry(interaction: discord.Interaction, number: int):
        if gSheet.deleteEntry(number):
            return await interaction.response.send_message(f'Problem #{number} has been deleted.', ephemeral=True, delete_after=15)
        else:
            return await interaction.response.send_message(f'Problem #{number} could not be deleted.', ephemeral=True, delete_after=15)
        
    client.run(config.token)

if __name__ == "__main__":
    main()