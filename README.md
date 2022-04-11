# callToWhatsapp
### Overview of My Submission
Some times we can not answer calls and can't respond to them on call for some time, so instead of rejecting their call and telling them to text, we get thier messege and convert it to text and whatsapp it to our own number.

### Prerequisites

* python
* DeepGram API key
* Twilio Python Helper Library
* Twilio WhatsApp sandbox
* Subscribed to twilio whatsapp sandbox from your number

<!-- [Note:] # Screenshots/demo videos are encouraged! -->
### Installation

Export Following environment variables

* RECORD_STS_WEBHOOK
* TWILIO_ACCOUNT_SID
* RECORD_STS_WEBHOOK (webhook URL for recording status updates)
* DEEPGRAM_API_KEY
* TWILIO_WHATSAPP_NO
* PERSONAL_WHATSAPP_NO

Now run the flask app which is main.py

Now whenever someone calls your Twilio number Twilio will record the call and once the call ends our flask application will receive a webhook call.
Once our application receives a webhook called DeepGram will take the recording and returns the Text of that recording which will be sent to our number via WhatsApp.


![Whatsapp msg](https://user-images.githubusercontent.com/60034233/162704133-7fca1b5b-9e95-4e77-9d97-4ccb34fb19ca.jpeg)


