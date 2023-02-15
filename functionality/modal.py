import discord
from discord import app_commands
from discord.ext import commands, tasks
import gspread
import config

class LeetcodeEntry(discord.ui.Modal, title="Leetcode Information Entry"):
    # Column Headers ['Number', 'Problem', 'Type', 'Solution Details', 'Link', 'Review']
    number = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Number",
        placeholder="Leetcode number"
    )
    problem = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Number",
        placeholder="Leetcode number"
    )

    