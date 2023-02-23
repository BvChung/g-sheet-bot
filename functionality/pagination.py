import discord
from functionality import *

class PaginatedView(discord.ui.View):
    
    def __init__(self, embedFactory: Embeds, data: list[dict], currentPage: int, currentIndex:int, itemsPerPage: int):
        super().__init__(timeout=200)
        self.embedFactory = embedFactory
        self.data = data
        self.currentPage = currentPage
        self.currentIndex = currentIndex
        self.itemsPerPage = itemsPerPage

    @discord.ui.button(label='<', style=discord.ButtonStyle.blurple)
    async def prev(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.currentPage - 1 >= 1:
            self.currentPage -= 1
            self.currentIndex -= self.itemsPerPage
            embed = self.embedFactory.paginatedEmbed(self.data, self.currentPage, self.currentIndex, self.itemsPerPage)
            await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label='>', style=discord.ButtonStyle.blurple)
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.currentIndex + self.itemsPerPage < len(self.data):
            self.currentPage += 1
            self.currentIndex += self.itemsPerPage
            embed = self.embedFactory.paginatedEmbed(self.data, self.currentPage, self.currentIndex, self.itemsPerPage)
            await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label='>|', style=discord.ButtonStyle.blurple)
    async def toLast(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.currentIndex + self.itemsPerPage < len(self.data):
            self.currentPage += 1
            self.currentIndex += self.itemsPerPage
            embed = self.embedFactory.paginatedEmbed(self.currentPage, self.currentIndex, self.itemsPerPage, self.data)
            await interaction.response.edit_message(embed=embed, view=self)

    def on_timeout(self) -> None:
        print("timeout")
        return 