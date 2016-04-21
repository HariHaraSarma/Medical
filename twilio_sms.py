# Account SSID : AC0422c13979a9f3207aae6fe4366a32ca
# API KEY  :  a43022ddcac0a4136d06f9261eda6a0c
# Number : +15734644113

from twilio.rest import TwilioRestClient 
 
# put your own credentials here 

def send_sms(to_, body):
	ACCOUNT_SID = "AC0422c13979a9f3207aae6fe4366a32ca" 
	AUTH_TOKEN = "a43022ddcac0a4136d06f9261eda6a0c" 
	 
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
	 
	client.messages.create(
		to=to_, 
		from_="+15734644113", 
		body=body)

# send_sms('+919533977887', 'Test SMS sent from Python code')