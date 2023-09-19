import discord
from dotenv import load_dotenv
import os
from time import time
import sendRequest 

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
token = os.getenv("DISCORD_API_TOKEN")

@client.event
async def on_voice_state_update(member, before, after):

  #入室の場合
  if (before.channel is None) and (after.channel is not None):
    entranceInfo = {
      "timestamp": time(),
      "event": "entrance",
      "userId": str(member.id),
      "userName": member.name,
      "channelId": str(after.channel.id),
      "channelName": after.channel.name,
    }
    response = sendRequest.PostToSpreadSheet(entranceInfo)
    print(response)

  #退出の場合
  if (before.channel is not None) and (after.channel is None):
    exitInfo = {
      "timestamp": time(),
      "event": "exit",
      "userId": str(member.id),
      "userName": member.name,
      "channelId": str(before.channel.id),
      "channelName": before.channel.name,
    }
    response = sendRequest.PostToSpreadSheet(exitInfo)
    print(response)

  return

client.run(token)
