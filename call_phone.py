from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC054066343f0c18eb6619c2478a08e1c9"
# Your Auth Token from twilio.com/console
auth_token  = "1b0c20b27168fc4323dfbb629c99124e"


client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+8860935382210", 
    from_="+18136963318",
    body="Hello from Python!")

print(message.sid)

