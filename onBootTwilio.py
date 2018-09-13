#!/usr/bin/python3

# /usr/bin/python3   /home/bradb/onBootTwilio.py




# SLOPPY SCRIPT



# Check if online 

import sys
from urllib.request import urlopen


queryAccepted=False
while queryAccepted != True:
  try:
    urlopen("https://www.google.com/")
    queryAccepted = True
  except Exception as e:
    print("Internet not setup yet: %s" % e)
    sys.exit(1)

print("Out of loop and online")

# Not worried about race conditions and stuff




from twilio.rest import Client

account_sid = 'ACe2c87c947c1be98d6ff4567d32073d15'
auth_token = '98db6019853285576413f55075bd359a'
client = Client(account_sid, auth_token)


txtMsg = "AC ON/Desktop Boot Message"
fromNumber='+18313461358'

message = client.messages.create(
body=txtMsg,
from_=fromNumber,
to='+16194584207'
)


message = client.messages.create(
body=txtMsg,
from_=fromNumber,
to='+15418216121'
)


print("%s Sent" % txtMsg)
print(message.sid)


sys.exit(0)