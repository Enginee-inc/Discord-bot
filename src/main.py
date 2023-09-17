import discord
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents)
token = os.getenv("DISCORD_API_TOKEN")

@client.event
async def on_entry():
  return 

client.run(token)
