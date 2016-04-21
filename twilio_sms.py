from twilio.rest import TwilioRestClient 

# Account SSID : AC0422c13979a9f3207aae6fe4366a32ca
# API KEY  :  a43022ddcac0a4136d06f9261eda6a0c
# Number : +15734644113

def send_sms(to_, body):
	ACCOUNT_SID = "AC0422c13979a9f3207aae6fe4366a32ca" 
	AUTH_TOKEN = "a43022ddcac0a4136d06f9261eda6a0c" 
	 
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
	 
	client.messages.create(
		to=to_, 
		from_="+15734644113", 
		body=body)
