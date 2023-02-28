import discord

class Embeds:
    def __init__(self) -> None:
        pass

    def createEmbed(self, data: list[dict], title:str, currentPage:int, start:int, itemsPerPage: int):
        embed = discord.Embed(title=title, color=discord.Colour.orange(), description=f'Page {currentPage}')
        end = start + itemsPerPage
        
        # for row in data[start: end]:
        for row in data[start: end]:
            problem = str(row['Number']) + '. ' + str(row['Name']) + ' ' + '[' + str(row['Topic']) + ': '

            if (str(row['Review']) == 'yes'):
                problem = '⭐ ' + problem

            if (str(row['Difficulty']) == 'Easy'):
                problem = problem + row['Difficulty'] + ' 🟩]'
            elif (str(row['Difficulty']) == 'Medium'):
                problem = problem + row['Difficulty'] + ' 🟨]'
            elif (str(row['Difficulty']) == 'Hard'):
                problem = problem + row['Difficulty'] + ' 🟥]'

            solution = 'Solution: ' + str(row['Solution'])
            link = 'Link: ' + str(row['Link'])
            output = f'{link}\n{solution}'
            embed.add_field(name=problem, value=output, inline=False)

        return embed
    
    def helpCommand(self):
        embed = discord.Embed(title='leetBot Commands', color=discord.Colour.random(), description='All available commands.')
        embed.add_field(name='/newentry', value='', inline=False)
        return embed