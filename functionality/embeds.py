import discord

class Embeds:
    def __init__(self) -> None:
        self.color = discord.Colour.random()

    def defaultEmbed(self, data: list[dict]):
        embed = discord.Embed(title="All Problems", color=self.color)
        for row in data:
            problem = str(row['Number']) + '. ' + row['Name'] + ' ' + '[' + row['Category'] + ']'
            if (row['Review'] == 'yes'):
                problem = '⭐ ' + problem

            solution = 'Solution: ' + row['Solution']
            link = 'Link: ' + row['Link']
            output = f'{link}\n{solution}'
            embed.add_field(name=problem, value=output, inline=False)

        return embed
    
    def categoryEmbed(self, category: str, data: list[dict]):
        embed = discord.Embed(title=category, color=self.color)
        for row in data:
            problem = str(row['Number']) + '. ' + row['Name']
            if (row['Review'] == 'yes'):
                problem = '⭐ ' + problem

            solution = 'Solution: ' + row['Solution']
            link = 'Link: ' + row['Link']
            output = f'{link}\n{solution}'
            embed.add_field(name=problem, value=output, inline=False)

        return embed
    
    def paginatedEmbed(self, data: list[dict], currentPage:int, currentIndex:int, itemsPerPage: int):
        embed = discord.Embed(title="All Problems", color=self.color, description=f'Page {currentPage}')
        for row in data[currentIndex:currentIndex + itemsPerPage]:
            problem = str(row['Number']) + '. ' + row['Name'] + ' ' + '[' + row['Category'] + ']'
            if (row['Review'] == 'yes'):
                problem = '⭐ ' + problem

            solution = 'Solution: ' + row['Solution']
            link = 'Link: ' + row['Link']
            output = f'{link}\n{solution}'
            embed.add_field(name=problem, value=output, inline=False)

        return embed
    