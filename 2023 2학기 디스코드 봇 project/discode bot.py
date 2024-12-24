import discord
from discord import app_commands 


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: 
            await tree.sync() 
            self.synced = True
        print(f'{self.user}이 시작되었습니다')
        game = discord.Game('ㅎㅇ')
        await self.change_presence(status=discord.Status.idle, activity=game)


client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = 'ryan', description='예문입니다') 
async def slash2(interaction: discord.Interaction):
        await interaction.response.send_message('succeeded', ephemeral=False)

@tree.command(name = 'iutube', description='아이유 영상') 
async def slash2(interaction: discord.Interaction):
        await interaction.response.send_message('https://www.youtube.com/watch?v=fdJLdQFgDiM&t=19s', ephemeral=False)

@tree.command(name = 'insta', description='아이유 인스타') 
async def slash2(interaction: discord.Interaction):
        await interaction.response.send_message('https://www.instagram.com/dlwlrma', ephemeral=False)

client.run('MTE0NzA1NDUwNTYzMjk4OTI3NA.G5aFGH.IvBF3cZhQystrp_0KgQP95FoTPofu30GrlgNqY')