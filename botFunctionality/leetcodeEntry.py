import discord
from .sheet import Sheet

# Column Headers ['Number', 'Name', 'topic', 'Solution', 'Link', 'Review']
TOPICS = ["Arrays", "2-Pointer", "Stack", "Binary Search", "Sliding Window", "Linked List", "Trees", "Tries", "Heap", "Intervals", "Greedy", "Backtracking", "Graphs", "1D-DP", "2D-DP", "Bit Manipulation", "Math"]
REVIEW = ['Yes', 'No']
DIFFICULTY = ['Easy', 'Medium', 'Hard']

class LeetcodeEntry(discord.ui.Modal):
    problemInfo = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Number, Name, Difficulty (Format=#;Name;Diff)",
        placeholder="Input number, name and difficulty",
        max_length=200
    )

    link = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Link",
        placeholder="Problem link",
        max_length=300
    )

    topic = discord.ui.TextInput(
        style=discord.TextStyle.paragraph,
        label="Topic (⚠️ Choose 1 option & follow format)",
        placeholder="Problem topic",
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
    
    def _validateInputs(self)->list:
        name = ""
        number = "" 
        difficulty = ""
        try:
            name, number, difficulty = str(self.problemInfo).split(';')
            difficulty = difficulty.capitalize()
        except:
            raise Exception('Invalid number + name + difficulty input. ⚠️\nFormat = #;Name;Difficulty')
        
        if not name or not number or not difficulty:
            raise Exception('Number, name or difficulty can not be blank.')
        
        if difficulty not in DIFFICULTY:
            raise Exception('Invalid difficulty input. ⚠️')
        
        if str(self.topic) not in TOPICS:
            raise Exception('Invalid topic input. ⚠️\nOptions: Arrays, 2-Pointer, Stack, Binary Search, Sliding Window, Linked List, Trees, Tries, Heap, Intervals, Greedy, Backtracking, Graphs, 1D-DP, 2D-DP, Bit Manipulation, Math')

        if str(self.review).capitalize() not in REVIEW:
            raise Exception('Invalid review input. ⚠️')

        return [number, name, difficulty.capitalize()]