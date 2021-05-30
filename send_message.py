
from twilio.rest import Client
from secret import twilio_Ouath_token, twilio_phoneNumber, twilio_account, cellphone

#step 1
# create an array of my messages
MORNING= ["hi! I miss you, have a great morning!", "hey how is your morning going?", "love youuu", "When you coming out to visit me? "]
NIGHT = ["goodnight!", "have a great night, hope to see you guy's soon!" ,"what you guys up to?"]


#step 2
#get API to send to a number 
def send_message(text=MORNING):
    account_sid = twilio_account
    auth_token  = twilio_Ouath_token

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=cellphone,
        from_= twilio_phoneNumber,
        body=text[2])

    print(message.sid)


# step 3
# assign the messages to send at a specific time.
# -----main------
send_message(MORNING)
