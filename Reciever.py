from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import pickle
dataval=["hi","u"]
app = Flask(__name__)
@app.route("/")
@app.route("/",methods=['POST'])

def sms_reply():
    data=open("data.txt","wb")
    msg = request.form.get('Body')
    dataval[0]=msg
    pickle.dump(dataval,data)
    data.close()
    print(dataval)
    return(msg)

if __name__ == "__main__":
    app.run(debug=True)