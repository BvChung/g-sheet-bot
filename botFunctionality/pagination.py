import discord
from abc import ABC, abstractmethod
from .embeds import Embeds
from .sheet import Sheet

class PaginatedView(discord.ui.View, ABC):
    def __init__(self, gSheet: Sheet, embedFactory: Embeds, data: list[dict], title:str, currentPage: int, currentIndex:int, itemsPerPage: int):
        super().__init__(timeout=200)
        self.gSheet = gSheet
        self.embedFactory = embedFactory
        self.data = data
        self.title = title
        self.currentPage = currentPage
        self.currentIndex = currentIndex
        self.itemsPerPage = itemsPerPage

    @discord.ui.button(label='|<', style=discord.ButtonStyle.secondary, disabled=True)
    async def toFirstPageBtn(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.currentPage = 1
        self.currentIndex = 0
        await self.updateView(interaction)

    @discord.ui.button(label='<', style=discord.ButtonStyle.blurple, disabled=True)
    async def prevPageBtn(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.currentPage -= 1
        self.currentIndex -= self.itemsPerPage
        await self.updateView(interaction)

    @discord.ui.button(label='>', style=discord.ButtonStyle.blurple)
    async def nextPageBtn(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.currentPage += 1
        self.currentIndex += self.itemsPerPage
        await self.updateView(interaction)

    @discord.ui.button(label='>|', style=discord.ButtonStyle.secondary)
    async def toLastPageBtn(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.currentPage = (len(self.data) // self.itemsPerPage)
        self.currentIndex = len(self.data) - self.itemsPerPage
        await self.updateView(interaction)
    
    @discord.ui.button(label='🔃 Refresh', style=discord.ButtonStyle.blurple)
    async def refreshBtn(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.refreshData()
        self.currentPage = 1
        self.currentIndex = 0
        await self.updateView(interaction)

    async def updateView(self, interaction: discord.Interaction):
        embed = self.embedFactory.createEmbed(self.data, self.title, self.currentPage, self.currentIndex, self.itemsPerPage)
        self.updateBtns()
        await interaction.response.edit_message(embed=embed, view=self)

    @abstractmethod
    def refreshData(self):
        pass

    def updateBtns(self):
        if self.currentPage == 1:
            self.prevPageBtn.disabled = True
            self.toFirstPageBtn.disabled = True
            self.nextPageBtn.disabled = False
            self.toLastPageBtn.disabled = False
        elif self.currentIndex + self.itemsPerPage >= len(self.data) - 1:
            self.nextPageBtn.disabled = True
            self.toLastPageBtn.disabled = True
            self.prevPageBtn.disabled = False
            self.toFirstPageBtn.disabled = False
        else:
            if self.prevPageBtn.disabled and self.toFirstPageBtn.disabled:
                self.prevPageBtn.disabled = False
                self.toFirstPageBtn.disabled = False
            
            if self.nextPageBtn.disabled and self.toLastPageBtn.disabled:
                self.nextPageBtn.disabled = False
                self.toLastPageBtn.disabled = False
            
    def on_timeout(self) -> None:
        print("timeout")
        return 
    