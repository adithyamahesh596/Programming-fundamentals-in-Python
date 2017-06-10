from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACe59157deada4e83e4471bd72152d8d45"
# Your Auth Token from twilio.com/console
auth_token  = "48507d92c8dd3d5813b1e8e67da0b651"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14086567994", 
    from_="+14087676787",
    body="Your phone has been hacked please pay 159000 dollars to clean your phone")

print(message.sid)
