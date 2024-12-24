import discord, random, openpyxl
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
        game = discord.Game('T_Bot')
        await self.change_presence(status=discord.Status.idle, activity=game)


client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = '정보저장', description='info') 
async def slash2(interaction: discord.Interaction, 이름:str, 나이:int):
    fill = openpyxl.load_workbook('Info.xlsx')
    sheet = fill.active
    i=1
    while True:
            if sheet["A" + str(i)].value == str(f'{interaction.user.id}'):
                sheet["B" + str(i)].value = str(f'{이름}')
                sheet["C" + str(i)].value = str(f'{나이}')
                fill.save("Info.xlsx")
                await interaction.response.send_message(f'{interaction.user.mention} 정보가 변경되었습니다.', ephemeral=False)
                break

            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(f'{interaction.user.id}')
                sheet["B" + str(i)].value = str(f'{이름}')
                sheet["C" + str(i)].value = str(f'{나이}')
                fill.save("Info.xlsx")
                await interaction.response.send_message(f'{interaction.user.mention} 저장되었습니다.', ephemeral=False)
                break
            i += 1

@tree.command(name = '정보초기화', description='reset') 
async def slash2(interaction: discord.Interaction, 이름:str):
    fill = openpyxl.load_workbook(str(f'{이름}')+'.xlsx')
    sheet = fill.active
    i=1
    while True:
            if sheet["A" + str(i)].value == None:
                await interaction.response.send_message(f'완료되었습니다. ||{interaction.user.mention}||', ephemeral=False)
                fill.save(str(f'{이름}')+".xlsx")
                break
            else:
                sheet["A" + str(i)].value = None
                sheet["B" + str(i)].value = None
                sheet["C" + str(i)].value = None
            i += 1

@tree.command(name = '홀짝', description='game') 
async def slash2(interaction: discord.Interaction, 홀짝:str, 배팅금:int):
    fill = openpyxl.load_workbook('money.xlsx')
    sheet = fill.active
    i=1
    number=random.randint(1,2)
    if str(f'{홀짝}')=='홀':
         if number==1:
              success=1
         else:
              success=0
              fail='짝'
    elif str(f'{홀짝}')=='짝':
         if number==2:
              success=1
         else:
              success=0
              fail='홀'
    while True:
            if sheet["A" + str(i)].value == str(f'{interaction.user.id}'):
                if int(f'{배팅금}')<=sheet["B" + str(i)].value:
                    if success==1:
                        sheet["B" + str(i)].value += int(f'{배팅금}')
                        await interaction.response.send_message(str(f'{홀짝}')+f'✨\n`+' + str(f'{배팅금}') + '💵`', ephemeral=False)
                    else:
                        sheet["B" + str(i)].value -= int(f'{배팅금}')
                        await interaction.response.send_message(fail+f'🧨\n`-' + str(f'{배팅금}') + '💵`', ephemeral=False)
                else:
                     await interaction.response.send_message(f'돈이 부족합니다.\n`'+str(sheet["B" + str(i)].value)+'💰`', ephemeral=False)
                fill.save("money.xlsx")
                break

            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(f'{interaction.user.id}')
                sheet["B" + str(i)].value = 1000
                if int(f'{배팅금}')<=sheet["B" + str(i)].value:
                    if success==1:
                        sheet["B" + str(i)].value += int(f'{배팅금}')
                        await interaction.response.send_message(f'성공✨\n`+' + str(f'{배팅금}') + '💵`', ephemeral=False)
                    else:
                        sheet["B" + str(i)].value -= int(f'{배팅금}')
                        await interaction.response.send_message(f'실패🧨\n`-' + str(f'{배팅금}') + '💵`', ephemeral=False)
                else:
                     await interaction.response.send_message(f'돈이 부족합니다.\n`'+str(sheet["B" + str(i)].value)+'💰`', ephemeral=False)
                fill.save("money.xlsx")
                break
            i += 1

client.run('MTEwNjIyNDIzOTk5ODE0NDU5Mw.GpVkhu.K7fqb-A8dysY6ZUrpYPC8p0wcrglFUtkhcIGrY')