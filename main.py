import discord
import os 
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True

client = discord.Client(intents=intents)

TOKEN = os.getenv("TOKEN")
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID"))

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_member_update(before, after):
    added_roles = [r for r in after.roles if r not in before.roles]
    
    for role in added_roles:
        channel = client.get_channel(LOG_CHANNEL_ID)
        await channel.send(f"Name: **{after.display_name}**\n Role: **{role.name}**!")

client.run(TOKEN)

