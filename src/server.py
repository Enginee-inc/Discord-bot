from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from os import getenv


class Server(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header("User-Agent", "discord-app")
    self.end_headers()
    
ip =  getenv("SERVER_ADDRESS") or "127.0.0.1"
port = 3000

server = HTTPServer((ip,port),Server) 

server.serve_forever()