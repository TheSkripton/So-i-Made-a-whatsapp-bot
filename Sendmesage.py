from twilio.rest import Client 

def sendmessage(Message):   
    account_sid = 'your account no' 
    auth_token = 'your authtoken' 
    client = Client(account_sid, auth_token) 
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body=Message,      
                                to='whatsapp:+919482465825' 
                            ) 
    print(message.sid)
sendmessage("Working")