import discord

class Embeds:
    def __init__(self) -> None:
        self.difficulty = {
            'Easy': '🟩',
            'Medium': '🟨',
            'Hard': '🟥'
        }

    def create_data_embed(self, data: list[dict], title:str, current_page:int, starting_index:int, items_per_page: int):
        embed = discord.Embed(title=title, color=discord.Colour.random(), description=f'Page {current_page}')
        ending_index = starting_index + items_per_page
        if ending_index >= len(data):
            ending_index = len(data)
        
        for i in range(starting_index, ending_index):
            problem = str(data[i]['Number']) + '. ' + str(data[i]['Name']) + ' ' + '[' + str(data[i]['Topic']) + ': ' + str(data[i]['Difficulty'])

            if (str(data[i]['Review']) == 'Yes'):
                problem = '⭐ ' + problem
            
            difficulty = self.difficulty[data[i]['Difficulty']]
            problem += ' ' + difficulty + ']'

            solution = 'Solution: ' + str(data[i]['Solution'])
            link = 'Link: ' + str(data[i]['Link'])
            output = f'{link}\n{solution}'
            embed.add_field(name=problem, value=output, inline=False)

        return embed
    
    def create_help_embed(self, commands: list[dict]):
        embed = discord.Embed(title='leetBot Commands', color=discord.Colour.red())

        for cmd in commands:
            name = cmd['name']
            description = cmd['description']
            embed.add_field(name=name, value=description, inline=False)
        
        return embed