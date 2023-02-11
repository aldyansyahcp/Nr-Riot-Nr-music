from telethon.tl.functions.messages import GetDialogsRequest
from telethon import TelegramClient, sync, events
from telethon import utils
from telethon import functions
import csv, time, random, re, datetime, requests, bs4, base64, os

apid = "22473095"
api_hashcodec = "349f33c335386adb28d132067610bd6f"
client = TelegramClient("session/adli",apid,api_hashcodec).start()
client.parse_mode = None
ses = requests.Session()
ua = ['Mozilla/5.0 (X11; CrOS x86_64 13310.76.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.108 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 11895.118.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.159 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12239.92.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.136 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 13099.110.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.136 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 13099.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.127 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 13020.87.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.119 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12499.66.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.106 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 13310.59.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.84 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12739.111.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12607.82.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.123 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 13099.85.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.110 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12607.58.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.86 Safari/537.36']
ses.headers = {
    'User-Agent': random.choice(ua),
    'Cache-Control':'max-age=0'
    } 

result = {
    "me": str(client.get_me()),
    "user": [],
    "group": [],
    "mem_group": [],
    "anything":[],
}


for x,i in enumerate(client.get_dialogs(),1):
        if len(i.name) != 0:
            en = i.entity
            if i.is_user:
                output = f" {i.name}, {en.id}, {en.username}, {en.access_hash}, {en.phone}"
                result["user"].append(output)
            if i.is_group:
                output = f" {i.name}, {en.id}, {en.participants_count}"
                print(output)
                result["group"].append(output)
                
def sendlaporan(msg):
    cet = msg.chat.id
    tek = "".join(msg.text).split(",")
    client.parse_mode = "html"
    lap = "CH {} Done\nIJIN START CH {} @bogelhaga @Estu_21\n<b><i>this message send from Bot auto generated @Ruprechkz_bot</i></b>".format(tek[0], tek[1])
    client.send_message(878038917, lap)
    bot.send_message(cet, "laporan terkirim")
    
            
def sendnrmusic(msg):
    cet = msg.chat.id
    tek = "".join(msg.text)
    bot.send_message(cet, "Sorry you dont have acces to this Bot")
    
def getmemgroup(idgroup):
    mem = client.get_participants(idgroup, aggressive=True)
    allmem = [f"{i.id}, {i.first_name} {i.last_name}, {i.phone}, {i.username}, {i.access_hash}" for i in mem]
    global iduser
    iduser = open("ytmusicsatu.txt","r").read().replace("\n",",")[2:-1].split(",") #ytmusic iduser
    #iduser = open("ytriotsatu.txt","r").read().split("\n")
    faker = True
    while faker:
        getm = client.get_messages(idgroup, limit=3000)
        #date = datetime.datetime.now().strftime("%d-%b-%Y, %H:%M")
        rez = {
            "msg":""
        }
        getm.reverse()
        for x in iduser:
            for i in getm:
                if i.date.date() == datetime.datetime.now().date():
                    #print(i.sender_id == x, x)
                    #print(i.date.date() == datetime.datetime.now().date())
                    if i.sender.first_name == "新acahyo":
                    #if i.sender_id == int(x):
                        rede = f"\t{i.sender.first_name} {i.sender.last_name}, {i.message}, {i.date.hour}:{i.date.minute}\n"
                        rez["msg"]+=rede
#                    else:
#                        print(i.sender_id == datetime.datetime.now().date(), "some id false")
#                        faker = False
#                else:
#                    print(i.date.date() == datetime.datetime.now().date(), "datetime false")
#                    faker = False
        if len(rez["msg"]) != 0:
            os.system("clear")
            #print(result["user"])
            print(rez["msg"], datetime.datetime.now().strftime("%d-%b-%Y, %H:%M"))
            rez.clear()
            time.sleep(200)
            continue
        else:
            print("msg is none zero",datetime.datetime.now().strftime("%d-%b-%Y, %H:%M"))
            time.sleep(180)
            continue

def getusgp(id):
    getuser = client.get_participants(id, aggressive=True)
    global iduser
    iduser = []
    for i in getuser:
        iduser.append(i.id)
    
if __name__ == "__main__":
    print("\n\t BOT Started with telethon",datetime.datetime.now().strftime("%d-%b-%Y, %H:%M"))
    getmemgroup(878038917) #NR YTMUSIC
    #getusgp(885961405)    ;getmemgroup(885961405) #NR Riot
    
