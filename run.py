import discord
import os
from discord import app_commands
from dotenv import load_dotenv
from os.path import join, dirname
import random

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
TOKEN = os.getenv("TOKEN")

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = MyClient()

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

EMOJI_IDS = {
    1: 'dice1:1260035148720771174',
    2: 'dice2:1260035151027638322',
    3: 'dice3:1260035153426776124',
    4: 'dice4:1260035155704418374',
    5: 'dice5:1260035157914550272',
    6: 'dice6:1260035160599167027'
}

@client.tree.command(name='dice')
@app_commands.describe(sides="ダイスの数")
async def create_custom(interaction: discord.Interaction, sides: app_commands.Range[int, 1, 20]):
    """ダイス振れます"""
    results = []
    stamps = ""
    for _ in range(sides):
        result = random.randint(1, 6)
        results.append(result)
        emoji_name, emoji_id = EMOJI_IDS[result].split(':')
        stamps += f'<:{emoji_name}:{emoji_id}> '

    await interaction.response.send_message(content=f'結果: {results}')
    await interaction.channel.send(content=stamps)

client.run(TOKEN)
