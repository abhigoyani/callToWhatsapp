from flask import Flask,request

from call_to_txt import conTXT,sendWhatsapp
import os
import json
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse



account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

app = Flask("__main__")



@app.route("/")
def home():
  return "home"


@app.route("/voice",methods=['GET', 'POST'])
def recordIncomingCall():

  response = VoiceResponse()
  response.say('Hello. Please leave a message after the beep.')
  response.record()
  response.recording_status_callback(os.environ["RECORD_STS_WEBHOOK"])
  
  return str(response)

@app.route("/recordWeb",methods=['GET', 'POST'])
def recordSts():
  body = json.loads(request.data)
  if(body.recording_status_callback_event == "completed"):
    msg =  conTXT(body["audio_url"])
    msgSID = sendWhatsapp(msg)
    
  return json.loads(msgSID)


app.run(host="0.0.0.0",port=6969)


