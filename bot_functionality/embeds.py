import discord


class Embeds:
    def __init__(self) -> None:
        self.embed_color = {
            'Default': discord.Colour.blurple(),
            'Topic': discord.Colour.blurple(),
            'Help': discord.Colour.red()
        }

    def create_data_embed(self, data: list[dict], title: str, current_page: int, starting_index: int, items_per_page: int, embed_type: str = "Default"):
        embed = discord.Embed(
            title=title, color=self.embed_color[embed_type], description=f'__**Page {current_page}**__')
        ending_index = starting_index + items_per_page
        if ending_index >= len(data):
            ending_index = len(data)

        for i in range(starting_index, ending_index):
            problem = str(data[i]['Number']) + '. ' + str(data[i]['Name'])

            link = '**Link:** ' + str(data[i]['Link'])

            solution = '```' + str(data[i]['Solution']) + '```'

            output = f'{link}\n{solution}\n'
            embed.add_field(name=problem, value=output, inline=False)

        return embed

    def create_help_embed(self, commands: list[dict]):
        embed = discord.Embed(title='leetBot Commands',
                              color=self.embed_color['Help'])

        for cmd in commands:
            name = cmd['name']
            description = cmd['description']
            embed.add_field(name=name, value=description, inline=False)

        return embed
