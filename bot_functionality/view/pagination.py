import discord
from abc import ABC, abstractmethod
from ..embeds import Embeds
from ..sheet import Sheet

class PaginatedView(discord.ui.View, ABC):
    def __init__(self, google_sheets: Sheet, embed_factory: Embeds, data: list[dict], title:str, current_page: int, current_index:int, items_per_page: int):
        super().__init__(timeout=None)
        self._google_sheets = google_sheets
        self._embed_factory = embed_factory
        self._data = data
        self.title = title
        self.current_page = current_page
        self.current_index = current_index
        self.items_per_page = items_per_page

    @discord.ui.button(label='|<', style=discord.ButtonStyle.secondary, disabled=True)
    async def to_first_page_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current_page = 1
        self.current_index = 0
        await self._update_view(interaction)

    @discord.ui.button(label='<', style=discord.ButtonStyle.blurple, disabled=True)
    async def previous_page_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current_page -= 1
        self.current_index -= self.items_per_page
        await self._update_view(interaction)

    @discord.ui.button(label='>', style=discord.ButtonStyle.blurple)
    async def next_page_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.current_index + self.items_per_page >= len(self._data):
            return await self._update_view(interaction)
        
        self.current_page += 1
        self.current_index += self.items_per_page
        await self._update_view(interaction)

    @discord.ui.button(label='>|', style=discord.ButtonStyle.secondary)
    async def to_last_page_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.current_index + self.items_per_page >= len(self._data):
            return await self._update_view(interaction)
        
        self.current_page = (len(self._data) // self.items_per_page)
        self.current_index = len(self._data) - self.items_per_page
        await self._update_view(interaction)
    
    @discord.ui.button(label='Refresh', style=discord.ButtonStyle.blurple)
    async def refresh_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.refresh_data()
        self.current_page = 1
        self.current_index = 0
        await self._update_view(interaction)

    @discord.ui.button(label='Exit', style=discord.ButtonStyle.red)
    async def exit_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.stop()
        await interaction.response.edit_message(view=self)

    @abstractmethod
    def refresh_data(self):
        pass

    async def _update_view(self, interaction: discord.Interaction):
        embed = self._embed_factory.create_data_embed(self._data, self.title, self.current_page, self.current_index, self.items_per_page)
        self._updateBtns()
        await interaction.response.edit_message(embed=embed, view=self)

    def _updateBtns(self):
        if self.current_page == 1 and self.current_index + self.items_per_page >= len(self._data):
            self.previous_page_button.disabled = True
            self.to_first_page_button.disabled = True
            self.next_page_button.disabled = True
            self.to_last_page_button.disabled = True
        elif self.current_page == 1:
            self.previous_page_button.disabled = True
            self.to_first_page_button.disabled = True
            self.next_page_button.disabled = False
            self.to_last_page_button.disabled = False
        elif self.current_index + self.items_per_page >= len(self._data):
            self.next_page_button.disabled = True
            self.to_last_page_button.disabled = True
            self.previous_page_button.disabled = False
            self.to_first_page_button.disabled = False
        elif self.previous_page_button.disabled and self.to_first_page_button.disabled and self.current_page > 1:
            self.previous_page_button.disabled = False
            self.to_first_page_button.disabled = False 
        elif self.next_page_button.disabled and self.to_last_page_button.disabled and self.current_index + self.items_per_page < len(self._data):
            self.next_page_button.disabled = False
            self.to_last_page_button.disabled = False
    
    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        return await interaction.response.send_message(error, ephemeral=True, delete_after=15)