import discord

class Embeds:
    def __init__(self) -> None:
        pass

    def createEmbed(self, data: list[dict], title:str, currentPage:int, start:int, itemsPerPage: int):
        embed = discord.Embed(title=title, color=discord.Colour.orange(), description=f'Page {currentPage}')
        end = start + itemsPerPage
        
        for row in data[start: end]:
            problem = str(row['Number']) + '. ' + str(row['Name']) + ' ' + '[' + str(row['Category']) + ']'
            if (str(row['Review']) == 'yes'):
                problem = '⭐ ' + problem

            solution = 'Solution: ' + str(row['Solution'])
            link = 'Link: ' + str(row['Link'])
            output = f'{link}\n{solution}'
            embed.add_field(name=problem, value=output, inline=False)

        return embed