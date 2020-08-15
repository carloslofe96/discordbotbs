import discord
from discord.ext import commands
import brawlstats
#client = discord.Client()
client= commands.Bot(command_prefix="!")
clientbs = brawlstats.Client('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjliZWY5MGY3LTI1ZjgtNGM4OS1hY2RiLWYzZWU2NzQ1NmYxZSIsImlhdCI6MTU5NzMzODQwNCwic3ViIjoiZGV2ZWxvcGVyLzhiMDgyMTJhLWVmYTItMGE2Mi0yMmQyLTY4YjgxYmY1MGUxOSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTkwLjUyLjE5Ni4xODciXSwidHlwZSI6ImNsaWVudCJ9XX0.guhG_it2hIOaUzeXvIZZcLNa-rUdMKZDCdE6vwX75l0r6ULZr-J2DIJrhRQ5AGhVzdmMdY67yz69PQSvSJGthQ')
lista=list()
contador=list()
contador.append(1)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    mytext = message.content
    myex = re.compile(r"(!torneo| )")
    final_str = re.sub(myex, '', mytext)
    x = final_str.split(",", 3)

    player1 = clientbs.get_profile(x[0])
    player2 = clientbs.get_profile(x[1])
    player3 = clientbs.get_profile(x[2])
    print(x)
    nlista = str(len(contador))

    if x[0] in lista:
        print('duplicado')
        await message.channel.send( player1.tag + "|  " + player1.name + " ya se encuentra en otro equipo")
    elif x[1] in lista:
        print('duplicado')
        await message.channel.send(player2.tag + "|  " + player2.name + " ya se encuentra en otro equipo")
    elif x[2] in lista:
        print('duplicado')
        await message.channel.send(player3.tag + "|  " + player3.name + " ya se encuentra en otro equipo")
    else:
        embed = discord.Embed(title="Equipo " + nlista, description=" ", colour=discord.Color.blue())
        embed.add_field(name=player1.name, value=player1.club.name)
        embed.add_field(name=player2.name, value=player2.club.name)
        embed.add_field(name=player3.name, value=player3.club.name)
        await message.channel.send(embed=embed)

        lista.append(x[0])
        lista.append(x[1])
        lista.append(x[2])
        contador.append([1])
        print(lista)

@client.command
async def torneo():
    on_message()

client.run('NzQzODc4NzY4NDAxMTg2ODE5.XzbFFg.8D8q-IQZPIZpSSaxjz7AEVL61Xo')

