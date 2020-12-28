import random
from datetime import date
import Arduinocommunication 
data=[]
responses=[]
def setup():
    data1=["greeting",["hello","hi","Good","morning","afternoon","night","its", "nice","meet","pleasure","to","you","whats" ,"new","yo","yooooo"],[0]]
    data2=["greetingquestion",["how","are","doing","you","doing?","are","you","fine?","well?","fine","well","doing","you?"],[0]]
    data3=["bye",["bye","byeee","hope ","you","had","a","good","time","nice","talking","to","you","goodbye","bye","see","later","soon","ive","got","to","get","going","must","im","in","a","rush","off"],[0]]
    data4=["selfwhat",["who","are","you","what","are","you?","what","is","whats","name","name"],[0]]
    data5=["selfmaker",["who","made","made","you","you?","whose","your","maker","maker","maker?","what"],[0]]
    data6=["insutl",["your","a","an","idiot","stupid","idiot","stupid","dumb","dumb"],[0]]
    data7=["date",["whats","what","is","the","date","day","today","date"],[0]]
    data8=["fanon",["fan","on","switch"],[0]]
    data9=["fanoff",["fan","off","of","switch"],[0]]
    data10=["lighton",["light","on","switch"],[0]]
    data11=["lightoff",["light","off","of","switch"],[0]]
    data12=["computeron",["computer","on","switch"],[0]]
    data13=["computeroff",["computer","off","of","switch"],[0]]
    data.append(data1)
    data.append(data2)
    data.append(data3)
    data.append(data4)
    data.append(data5)
    data.append(data6)
    data.append(data7)
    data.append(data8)
    data.append(data9)
    data.append(data10)
    data.append(data11)
    data.append(data12)
    data.append(data13)

    data1=["greeting",["Yo!","hello","Vamos","yolooo","HOLOOOO","Long time no see!!!","pleasure to meet you"]," "]
    data2=["bye",["I would not love to meet you again","Byee","Would Like to meet you again","see Y'a","Nice talking to you,bye","Hope not to meet you again","BYE.","That wa squite a short conversation","hope to see you again"]," "]
    data3=["greetingquestion",["Im Doing just as fine as i did yesterday","Fine","Im fine","Im doing good"]," "]
    data4=["selfwhat",["Im Ursula made by master Srkipton","Im Ursula!","my name is Ursula"]," "]
    data5=["selfmaker",["Im made by Master Skripton","Skripton","The great Skripton","Master Skripton, the great youtuber"]," "]
    data6=["insutl",["NOOOOOOOOOOOOOOOO you are","You insult me??, wait till robots take over the world, youll be the first one to be killed","wait till Elon finishes his work takes over the world with robots, your going to be the first one to die","Your going to regret"]," "]
    data7=["date",[],"date"]
    data8=["fanon",[],"fanon"]
    data9=["fanoff",[],"fanoff"]
    data10=["lighton",[],"lighton"]
    data11=["lightoff",[],"lightoff"]
    data12=["computeron",[],"compon"]
    data13=["computeroff",[],"compoff"]
    responses.append(data1)
    responses.append(data2)
    responses.append(data3)
    responses.append(data4)
    responses.append(data5)
    responses.append(data6)
    responses.append(data7)
    responses.append(data8)
    responses.append(data9)
    responses.append(data10)
    responses.append(data11)
    responses.append(data12)
    responses.append(data13)
def type(Sen):
    mostlytype=" "
    global data
    Sen=Sen.lower()
    Sen=Sen.split(" ")
    mostscore=0
    for List in data:
        for words in List[1]:
            if(List[2][0]>mostscore):
                mostscore=List[2][0]
                mostlytype=List[0]
            for senword in Sen:
                if senword==words:
                    List[2][0]=List[2][0]+1
    if(mostscore==0):
        mostlytype="dnms"
    for x in data:
        if(x!=0):
            x[2][0]=0
        else:
            x[2][0]=1
    return(mostlytype)

def response(typ):
    global responses
    for n in responses:
        if(typ!="dnms"):
            if(n[0]==typ and n[2]==" "):
                return(n[1][random.randint(0,len(n[1])-1)])
            elif(n[0]==typ and n[2]!=" "):
                return(dowork(n[2]))
        else:
            return("no")
def dowork(work):
    cr=["okay","doing","Will do","OKAY","Eh","Okay!"]
    if(work=="date"):
        return(date.today())
    if(work=="fanon"):
        Arduinocommunication.do('f')
        return(cr[random.randint(0,len(cr)-1)])
    if(work=="fanoff"):
        Arduinocommunication.do('F')
        return(cr[random.randint(0,len(cr)-1)])
    if(work=="lighton"):
        Arduinocommunication.do('L')
        return(cr[random.randint(0,len(cr)-1)])
    if(work=="lightoff"):
        Arduinocommunication.do('l')
        return(cr[random.randint(0,len(cr)-1)])
    if(work=="compon"):
        Arduinocommunication.do('c')
        return(cr[random.randint(0,len(cr)-1)])
    if(work=="compoff"):
        Arduinocommunication.do('C')
        return(cr[random.randint(0,len(cr)-1)])
def executeall(input):
    TyPE=type(input)
    Xesponse=response(TyPE)
    return(Xesponse)