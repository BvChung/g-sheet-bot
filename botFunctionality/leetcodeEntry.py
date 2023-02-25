import discord
import traceback
from .sheet import Sheet

# Column Headers ['Number', 'Name', 'Category', 'Solution', 'Link', 'Review']
CATEGORIES = ["Arrays", "2-Pointer", "Stack", "Binary Search", "Sliding Window", "Linked List", "Trees", "Tries", "Heap", "Intervals", "Greedy", "Backtracking", "Graphs", "1D-DP", "2D-DP", "Bit Manipulation", "Math"]
REVIEW = ['yes', 'no']

class LeetcodeEntry(discord.ui.Modal):
    numberAndName = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Number and Name (⚠️ Format: #-Name)",
        placeholder="Input using ",
        max_length=100
    )

    link = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Link",
        placeholder="Problem link",
        max_length=300
    )

    category = discord.ui.TextInput(
        style=discord.TextStyle.paragraph,
        label="Category (⚠️ Choose 1 option & follow format)",
        placeholder="Problem category",
        default="Arrays, 2-Pointer, Stack, Binary Search, Sliding Window, Linked List, Trees, Tries, Heap, Intervals, Greedy, Backtracking, Graphs, 1D-DP, 2D-DP, Bit Manipulation, Math",
        max_length=200
    )

    solution = discord.ui.TextInput(
        style=discord.TextStyle.paragraph,
        label="Solution",
        placeholder="Your solution",
        max_length=1000
    )

    review = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Review",
        placeholder="Input following format: yes or no",
        max_length=3
    )

    def __init__(self, *, title: str = ..., gSheet: Sheet) -> None:
        super().__init__(title=title)
        self.gSheet = gSheet