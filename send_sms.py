# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACec2b144a3d997d8d4c996bf403029b57"
auth_token = "0dfb8479096f8f6e94abcb7ff50a369b"
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(to="+525521022584",
                                             from_="+12014256278",
                                             body="Fuckoff!")