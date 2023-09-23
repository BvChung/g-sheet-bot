import discord
from discord import app_commands
from typing import Literal
from config import *
from bot_functionality import *

# test1


def main() -> None:
    discord_config = DiscordConfig()
    google_sheets_config = GoogleSheetsConfig()
    client = MyClient(discord_config.get_guild_id())
    google_sheets: Sheet = Sheet.get_state(google_sheets_config.get_credentials(
    ), google_sheets_config.get_sheet_name(), starting_column='A', ending_column='G')
    embed_factory = Embeds()

    @client.tree.command(description="Get all data")
    async def get_all(interaction: discord.Interaction):
        if DefaultView.is_active:
            try:
                found_message = await interaction.channel.fetch_message(DefaultView.message_id)
                return await interaction.response.send_message(f'There is already an active instance in #{found_message.channel} channel. ⚠️', ephemeral=True, delete_after=15)
            except Exception as error:
                print(error)
                DefaultView.is_active = False

        try:
            data = google_sheets.get_all_data()
        except Exception as error:
            return await interaction.response.send_message(error, ephemeral=True, delete_after=30)

        await interaction.response.send_message('Displaying data. ✅', ephemeral=True, delete_after=5)

        title, current_page, current_index, items_per_page = "All Problems", 1, 0, 5
        displayView = DefaultView(google_sheets, embed_factory,
                                  data, title, current_page, current_index, items_per_page)
        embed = embed_factory.create_data_embed(
            data, title, current_page, current_index, items_per_page)
        displayedMessage = await interaction.channel.send(embed=embed, view=displayView)
        DefaultView.is_active = True
        DefaultView.message_id = displayedMessage.id

        timeout = await displayView.wait()
        if not timeout:
            DefaultView.is_active = False
            DefaultView.message_id = None
            await displayedMessage.delete()

    @client.tree.command(description="Filter data by topic")
    @app_commands.describe(topic="Problem topic")
    async def get_topic(interaction: discord.Interaction, topic: Literal['Arrays', '2-Pointer', 'Stack', 'Binary Search', 'Sliding Window', 'Linked List', 'Trees', 'Tries', 'Heap', 'Intervals', 'Greedy', 'Backtracking', 'Graphs', '1D-DP', '2D-DP', 'Bit Manipulation', 'Math']):
        if TopicView.is_active:
            try:
                found_message = await interaction.channel.fetch_message(TopicView.message_id)
                return await interaction.response.send_message(f'There is already an active instance in #{found_message.channel} channel. ⚠️', ephemeral=True, delete_after=15)
            except Exception as error:
                print(error)
                TopicView.is_active = False

        try:
            data = google_sheets.filter_by_topic(topic)
        except Exception as error:
            return await interaction.response.send_message(error, ephemeral=True, delete_after=30)

        if not data:
            return await interaction.response.send_message('There are no entries with this topic. ⚠️', ephemeral=True, delete_after=15)

        await interaction.response.send_message('Displaying data. ✅', ephemeral=True, delete_after=5)

        current_page, current_index, items_per_page = 1, 0, 5
        displayView = TopicView(google_sheets, embed_factory, data,
                                topic, current_page, current_index, items_per_page)
        embed = embed_factory.create_data_embed(
            data, topic, current_page, current_index, items_per_page, "Topic")
        displayedMessage = await interaction.channel.send(embed=embed, view=displayView)
        TopicView.is_active = True
        TopicView.message_id = displayedMessage.id

        timeout = await displayView.wait()
        if not timeout:
            TopicView.is_active = False
            TopicView.message_id = None
            await displayedMessage.delete()

    @client.tree.command(description="Create new entry")
    async def create_entry(interaction: discord.Interaction):
        await interaction.response.send_modal(CreateEntry(title="New Leetcode Entry", google_sheets=google_sheets))

    @client.tree.command(description="Update entry")
    @app_commands.describe(number="Problem number")
    async def update_entry(interaction: discord.Interaction, number: int):
        try:
            row_information = google_sheets.get_entry(number)
        except Exception as error:
            return await interaction.response.send_message(error, ephemeral=True, delete_after=15)

        row_number: int = row_information[0]
        row_data: list = row_information[1]
        problem_info = str(row_data[0]) + ';' + row_data[1] + ';' + row_data[2]
        topic = str(row_data[3])
        solution = str(row_data[4])
        link = str(row_data[5])
        review = str(row_data[6])

        # Inject current entry's data into modal
        updateModal = UpdateEntry(
            title=f"Update Entry #{number}", google_sheets=google_sheets, row_number=row_number)
        updateModal.problem_info.default = problem_info
        updateModal.topic.default = topic
        updateModal.solution.default = solution
        updateModal.link.default = link
        updateModal.review.default = review

        await interaction.response.send_modal(updateModal)

    @client.tree.command(description="Delete entry")
    @app_commands.describe(number="Problem number")
    async def delete_entry(interaction: discord.Interaction, number: int):
        try:
            google_sheets.delete_entry(number)
        except Exception as error:
            return await interaction.response.send_message(error, ephemeral=True, delete_after=15)

        await interaction.response.send_message(f'Problem #{number} has been deleted. ✅', ephemeral=True, delete_after=15)

    @client.tree.command(description="Displays all available commands.")
    async def help(interaction: discord.Interaction):
        embed = embed_factory.create_help_embed(
            discord_config.get_commands_info())
        return await interaction.response.send_message(embed=embed, ephemeral=True)

    client.run(discord_config.get_token())


if __name__ == "__main__":
    main()
