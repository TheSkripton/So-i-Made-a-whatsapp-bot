import pickle
import time
import AI
import Sendmesage
oldmessage=" "
AI.setup()

while 1==1:
    time.sleep(1)
    newmessage=pickle.load(open("Ai\data.txt","rb"))
    messagetobesent=AI.executeall(newmessage[0])
    if(newmessage[1]=='u' and messagetobesent!="no"):
        Sendmesage.sendmessage(messagetobesent)
        newmessage=[newmessage[0],'r']
        pickle.dump(newmessage,open("Ai\data.txt","wb"))
        print(newmessage)
        print(messagetobesent)