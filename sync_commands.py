import discord
from discord import Client
from discord import app_commands
import numpy as np
import pandas as pd
from connections import GSheetInstance, SupabaseInstance
from bot_functionality import Embeds


def sync_commands(discord_client: Client, gsheet_client: GSheetInstance, supabase_client: SupabaseInstance, embed_factory: Embeds) -> Client:
    @discord_client.tree.command(description="Generate spreadsheet statistics.")
    async def get_stats(interaction: discord.Interaction):
        try:
            data = gsheet_client.get_all_rows()
        except Exception as error:
            return await interaction.response.send_message(error, ephemeral=True, delete_after=30)

        await interaction.response.send_message('Generating statistics. ✅', ephemeral=True, delete_after=5)

        df = pd.DataFrame(data[1:], columns=data[0])

        if 'Timestamp' in df.columns:
            df.drop(columns=['Timestamp'], inplace=True)

        numerical_columns_df = df.select_dtypes(include=[np.number])
        spreadsheet_name = gsheet_client.get_spreadsheet_filename()
        tab_name = gsheet_client.get_child_spreadsheet_name()

        stats = numerical_columns_df.describe().round(2)
        formatted_stats = f"```{stats.to_string()}```"

        embed = embed_factory.stats_embed(
            stats=formatted_stats, title=f'Base Spreadsheet: {spreadsheet_name}', name=f'{tab_name} Statistics')
        await interaction.channel.send(embed=embed)

    @discord_client.tree.command(description="Change to different spreadsheet.")
    @app_commands.describe(spreadsheet_key="Spreadsheet key located in the web url between d/ and /edit")
    async def change_spreadsheet(interaction: discord.Interaction, spreadsheet_key: str):
        try:
            gsheet_client.set_spreadsheet_key(spreadsheet_key)
        except Exception as error:
            message = f'Unable to change spreadsheet. ⚠️\n{error}'
            return await interaction.response.send_message(message, ephemeral=True, delete_after=15)

        new_spreadsheet_name = gsheet_client.get_spreadsheet_filename()
        await interaction.response.send_message(f'Changed to spreadsheet: {new_spreadsheet_name}. ✅')

    @discord_client.tree.command(description="Change to child spreadsheet in tabs by using gid.")
    @app_commands.describe(gid_key="GID key located in the web url after gid=")
    async def change_spreadsheet_gid(interaction: discord.Interaction, gid_key: int):
        try:
            gsheet_client.set_worksheet_gid(gid_key)
        except Exception as error:
            message = f'Unable to change different child spreadsheet. ⚠️\n{error}'
            return await interaction.response.send_message(message, ephemeral=True, delete_after=15)

        child_spreadsheet_name = gsheet_client.get_child_spreadsheet_name()
        await interaction.response.send_message(f'Changed to spreadsheet tab: {child_spreadsheet_name}. ✅')
    return discord_client
