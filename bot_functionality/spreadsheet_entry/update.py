import discord
import traceback
from .entry_modal import EntryModal
from ..sheet import Sheet


class UpdateEntry(EntryModal):
    def __init__(self, *, title: str, google_sheets: Sheet, row_number) -> None:
        super().__init__(title=title, google_sheets=google_sheets)
        self.row_number = row_number

    async def on_submit(self, interaction: discord.Interaction) -> None:
        number, name, difficulty = self._validate_inputs()

        try:
            self.google_sheets.update_entry(self.row_number, [[int(number), name, difficulty, str(
                self.topic), str(self.solution), str(self.link), str(self.review).capitalize()]])
        except Exception as error:
            return await interaction.response.send_message(error, ephemeral=True, delete_after=15)

        await interaction.response.send_message(f'Updated problem #{number}. ✅', ephemeral=True, delete_after=15)

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message(f'Issue: {error}.', ephemeral=True, delete_after=30)

        traceback.print_tb(error.__traceback__)
