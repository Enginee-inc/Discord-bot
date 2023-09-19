import discord
from dotenv import load_dotenv
import os
import sendRequest 
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import threading
import time

load_dotenv()

ADDRESS = "127.0.0.1"
PORT =5000

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "Hello, world!"
        self.wfile.write(bytes(message, "utf8"))
        return

httpd = ThreadingHTTPServer((ADDRESS, PORT), MyHandler)

intents = discord.Intents.default()

client = discord.Client(intents=intents)
token = os.getenv("DISCORD_API_TOKEN")

@client.event
async def on_voice_state_update(member, before, after):

  #入室の場合
  if (before.channel is None) and (after.channel is not None):
    entranceInfo = {
      "timestamp": time.time(),
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

if __name__ == "__main__":
   thread_1 = threading.Thread(target=httpd.serve_forever)
   thread_1.start()
   client.run(token)