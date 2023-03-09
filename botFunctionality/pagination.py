import discord
from abc import ABC, abstractmethod
from .embeds import Embeds
from .sheet import Sheet

class PaginatedView(discord.ui.View, ABC):
    def __init__(self, gSheet: Sheet, embedFactory: Embeds, data: list[dict], title:str, currentPage: int, currentIndex:int, itemsPerPage: int):
        super().__init__(timeout=None)
        self._gSheet = gSheet
        self._embedFactory = embedFactory
        self._data = data
        self.title = title
        self.currentPage = currentPage
        self.currentIndex = currentIndex
        self.itemsPerPage = itemsPerPage

    @discord.ui.button(label='|<', style=discord.ButtonStyle.secondary, disabled=True)
    async def toFirstPageBtn(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.currentPage = 1
        self.currentIndex = 0
        await self._updateView(interaction)

    @discord.ui.button(label='<', style=discord.ButtonStyle.blurple, disabled=True)
    async def prevPageBtn(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.currentPage -= 1
        self.currentIndex -= self.itemsPerPage
        await self._updateView(interaction)

    @discord.ui.button(label='>', style=discord.ButtonStyle.blurple)
    async def nextPageBtn(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.currentIndex + self.itemsPerPage >= len(self._data):
            return await self._updateView(interaction)
        
        self.currentPage += 1
        self.currentIndex += self.itemsPerPage
        await self._updateView(interaction)

    @discord.ui.button(label='>|', style=discord.ButtonStyle.secondary)
    async def toLastPageBtn(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.currentIndex + self.itemsPerPage >= len(self._data):
            return await self._updateView(interaction)
        
        self.currentPage = (len(self._data) // self.itemsPerPage)
        self.currentIndex = len(self._data) - self.itemsPerPage
        await self._updateView(interaction)
    
    @discord.ui.button(label='Refresh', style=discord.ButtonStyle.blurple)
    async def refreshBtn(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.refreshData()
        self.currentPage = 1
        self.currentIndex = 0
        await self._updateView(interaction)

    @discord.ui.button(label='Exit', style=discord.ButtonStyle.red)
    async def exitBtn(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.stop()
        await interaction.response.edit_message(view=self)

    @abstractmethod
    def refreshData(self):
        pass

    async def _updateView(self, interaction: discord.Interaction):
        embed = self._embedFactory.createDataEmbed(self._data, self.title, self.currentPage, self.currentIndex, self.itemsPerPage)
        self._updateBtns()
        await interaction.response.edit_message(embed=embed, view=self)

    def _updateBtns(self):
        if self.currentPage == 1 and self.currentIndex + self.itemsPerPage >= len(self._data):
            self.prevPageBtn.disabled = True
            self.toFirstPageBtn.disabled = True
            self.nextPageBtn.disabled = True
            self.toLastPageBtn.disabled = True
        elif self.currentPage == 1:
            self.prevPageBtn.disabled = True
            self.toFirstPageBtn.disabled = True
            self.nextPageBtn.disabled = False
            self.toLastPageBtn.disabled = False
        elif self.currentIndex + self.itemsPerPage >= len(self._data):
            self.nextPageBtn.disabled = True
            self.toLastPageBtn.disabled = True
            self.prevPageBtn.disabled = False
            self.toFirstPageBtn.disabled = False
        elif self.prevPageBtn.disabled and self.toFirstPageBtn.disabled and self.currentPage > 1:
            self.prevPageBtn.disabled = False
            self.toFirstPageBtn.disabled = False 
        elif self.nextPageBtn.disabled and self.toLastPageBtn.disabled and self.currentIndex + self.itemsPerPage < len(self._data):
            self.nextPageBtn.disabled = False
            self.toLastPageBtn.disabled = False
    
    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        return await interaction.response.send_message(error, ephemeral=True, delete_after=15)