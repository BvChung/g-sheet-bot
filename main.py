import discord
from discord import app_commands, ui, Embed
from discord.ext import commands, tasks
import config
import functionality

def main():
    client = functionality.MyClient.getClientState()
    gs = functionality.GSheet.getGSheetState()

    @client.tree.command()
    # @app_commands.rename(first="1st")
    @app_commands.describe(first="First number", second="Second number")
    @app_commands.choices(first=[app_commands.Choice(name="one", value=1), app_commands.Choice(name="two", value=2)])
    async def add(interaction: discord.Interaction, first:int, second:int):
        print(gs.leetcodeSheet.sheet1.get_all_records())
        await interaction.response.send_message(f'{first} + {second} = {first + second}')

    client.run(config.token)

    # gc = gspread.service_account_from_dict(config.credentials)
    # leetcodeSheet = gc.open(config.sheetName)
    # gc = gspread.service_account(config.secretJSON)
    # Column Headers ['Number', 'Problem', 'Type', 'Solution Details', 'Link', 'Review']
    # newRow = [49, "Group Anagrams", "Arrays", "Use a hashmap with key: [the count of number of letters in the alphabet using ascii ord(curr char) - ord('a') indexed from 0-25] and value: [grouped anagrams]", 'https://leetcode.com/problems/group-anagrams/', 'no']

    # print(leetcodeSheet.sheet1.delete_rows())
    # print(leetcodeSheet.sheet1.insert_row(newRow, 2))
    # leetcodeSheet.sheet1.sort((1, 'asc'))
    # print(leetcodeSheet.sheet1.get_all_records())
    # print(leetcodeSheet.sheet1.row_values(2))

if __name__ == "__main__":
    main()
