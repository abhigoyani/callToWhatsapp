import requests
import os

from twilio.rest import Client

def conTXT(recording_url):
    deepgram_req = requests.post('https://api.deepgram.com/v1/listen?punctuate=true',headers={'Authorization': 'token ' + os.environ["DEEPGRAM_API_KEY"],"content-type": "application/json"},json={"url": recording_url})
    msg = deepgram_req.text
    return msg

def sendWhatsapp(msg):
  account_sid = os.environ['TWILIO_ACCOUNT_SID']
  auth_token = os.environ['TWILIO_AUTH_TOKEN']
  client = Client(account_sid, auth_token)
  message = client.messages.create(
                              body=msg,
                              from_='whatsapp:'+os.environ["TWILIO_WHATSAPP_NO"],
                              to='whatsapp:'+os.environ["PERSONAL_TWILIO_NO"]
                          )
  return message.sid


def getCaller(sid):
  call = client.calls(sid).fetch()
  return call.From
