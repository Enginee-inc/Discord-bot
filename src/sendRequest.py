from dotenv import load_dotenv
import os
import requests
import json


load_dotenv()

def PostToSpreadSheet(data, header = {}):
  url = os.getenv('GAS_APP_URL')
  data = json.dumps(data)
  return requests.post(url =url, data=data, headers=header)

