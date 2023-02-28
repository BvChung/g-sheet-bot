import discord

class Embeds:
    def __init__(self) -> None:
        pass

    def createDataEmbed(self, data: list[dict], title:str, currentPage:int, start:int, itemsPerPage: int):
        embed = discord.Embed(title=title, color=discord.Colour.orange(), description=f'Page {currentPage}')
        end = start + itemsPerPage
        
        for row in data[start: end]:
            problem = str(row['Number']) + '. ' + str(row['Name']) + ' ' + '[' + str(row['Topic']) + ': ' + str(row['Difficulty'])

            if (str(row['Review']) == 'yes'):
                problem = '⭐ ' + problem
            
            match row['Difficulty']:
                case 'Easy':
                    problem = problem + ' 🟩]'
                case 'Medium':
                    problem = problem + ' 🟨]'
                case 'Hard':
                    problem = problem + ' 🟥]'

            solution = 'Solution: ' + str(row['Solution'])
            link = 'Link: ' + str(row['Link'])
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