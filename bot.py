import json
import time
import os

from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import ImportContactsRequest, DeleteContactsRequest
from telethon.tl.types import InputPhoneContact

load_dotenv()

api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
phone = os.environ.get("PHONE")
client = TelegramClient('verify_session', api_id, api_hash)
client.start(phone=phone)

hashmap = {}
target = ['+251986558241', '+251911611891', '+251911120867', '+251961281789', '+251961281790', '+251966030844']

for num in target:
    contact = InputPhoneContact(client_id=0, phone=num, first_name=num, last_name='User')
    result = client(ImportContactsRequest([contact]))
    if result.users:
        hashmap[num] = True
        client(DeleteContactsRequest(id=[num]))
    else:
        hashmap[num] = False
    time.sleep(1)

with open("output.json", "w") as file:
    json.dump(hashmap, file, indent=4)
print("Done")
