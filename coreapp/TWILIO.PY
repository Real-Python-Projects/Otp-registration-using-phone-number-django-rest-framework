
import os
from twilio.rest import Client


account_sid = 'ACdc1c1858d065412f288be22c0b814bf7'
auth_token = 'f154e9da85bc403ea9b4ab0488d24476'

client = Client(account_sid, auth_token)

msg = "Hello there!guys"
client.api.account.messages.create(
    to="+254717713943",
    from_="+18324153882",
    body=msg)