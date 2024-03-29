import discord
from ..sheet import Sheet


class EntryModal(discord.ui.Modal):
    problem_info = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Number, Name, Difficulty (Format=#;Name;Diff)",
        placeholder="Input number;name;difficulty",
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
        max_length=2000
    )

    review = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Review",
        placeholder="Input following format: yes or no",
        max_length=3
    )

    def __init__(self, *, title: str, google_sheets: Sheet) -> None:
        super().__init__(title=title)
        self.google_sheets = google_sheets
        self.TOPICS = ["Arrays", "2-Pointer", "Stack", "Binary Search", "Sliding Window", "Linked List", "Trees", "Tries",
                       "Heap", "Intervals", "Greedy", "Backtracking", "Graphs", "1D-DP", "2D-DP", "Bit Manipulation", "Math"]
        self.REVIEW = ['Yes', 'No']
        self.DIFFICULTY = ['Easy', 'Medium', 'Hard']

    def _validate_inputs(self) -> list:
        number = None
        name = None
        difficulty = None
        try:
            number, name, difficulty = str(self.problem_info).split(';')
        except:
            raise Exception(
                'Invalid number + name + difficulty input. ⚠️\nFormat = #;Name;Difficulty')

        if not name or not number or not difficulty:
            raise Exception('Number, name or difficulty can not be blank.')

        difficulty.capitalize()
        if difficulty not in self.DIFFICULTY:
            raise Exception('Invalid difficulty input. ⚠️')

        if str(self.topic) not in self.TOPICS:
            raise Exception('Invalid topic input. ⚠️\nOptions: Arrays, 2-Pointer, Stack, Binary Search, Sliding Window, Linked List, Trees, Tries, Heap, Intervals, Greedy, Backtracking, Graphs, 1D-DP, 2D-DP, Bit Manipulation, Math')

        if str(self.review).capitalize() not in self.REVIEW:
            raise Exception('Invalid review input. ⚠️')

        return [number, name, difficulty]
