import discord

class Embeds:
    def __init__(self) -> None:
        pass

    def createDataEmbed(self, data: list[dict], title:str, currentPage:int, start:int, itemsPerPage: int):
        embed = discord.Embed(title=title, color=discord.Colour.dark_teal(), description=f'Page {currentPage}')
        end = start + itemsPerPage
        if end >= len(data):
            end = len(data)
        
        for i in range(start, end):
        # for row in data[start: end]:
            problem = str(data[i]['Number']) + '. ' + str(data[i]['Name']) + ' ' + '[' + str(data[i]['Topic']) + ': ' + str(data[i]['Difficulty'])

            if (str(data[i]['Review']) == 'yes'):
                problem = '⭐ ' + problem
            
            match data[i]['Difficulty']:
                case 'Easy':
                    problem += ' 🟩]'
                case 'Medium':
                    problem += ' 🟨]'
                case 'Hard':
                    problem += ' 🟥]'

            solution = 'Solution: ' + str(data[i]['Solution'])
            link = 'Link: ' + str(data[i]['Link'])
            output = f'{link}\n{solution}'
            embed.add_field(name=problem, value=output, inline=False)

        return embed
    
    def createHelpEmbed(self, commands: list[dict]):
        embed = discord.Embed(title='leetBot Commands', color=discord.Colour.random())

        for cmd in commands:
            name = cmd['name']
            description = cmd['description']
            embed.add_field(name=name, value=description, inline=False)
        
        return embed