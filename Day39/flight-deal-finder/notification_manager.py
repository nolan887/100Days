from twilio.rest import Client
import os

TWILIO_SID = "AC96f51ba9845b52998cf4d9fdc593f577"
TWILIO_AUTH_TOKEN = os.environ.get("TWILLIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = "+16692013335"
TWILIO_VERIFIED_NUMBER = os.environ.get("MY_NUMBER")

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)