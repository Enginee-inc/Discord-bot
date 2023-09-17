from dotenv import load_dotenv
import os
import requests


load_dotenv()

def sendToSpreadSheet(data, header = {}):
  url = os.getenv('SPREAD_SHEET_URL')
  return requests.post(url, data, headers=header)

