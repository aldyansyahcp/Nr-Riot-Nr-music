
#telegram acahyo
from telethon.tl.functions.messages import GetDialogsRequest
from telethon import TelegramClient, sync, events
from telethon import utils
from telethon import functions
import csv, time, random, re, datetime

apid = "22473095"
api_hashcodec = "349f33c335386adb28d132067610bd6f"
client = TelegramClient("session/adli",apid,api_hashcodec).start()

result = {
    "account_name": str(client.get_me().first_name),
    "user": [],
    "group": [],
    "mem_group": [],
    "anything":[],
}

#print(ss.bot,ss.first_name, ss.last_name, ss.username, ss.access_hash, ss.phone, ss.id)

#print(f"{ss.first_name} {ss.last_name}\n{ss.id}")
# Listing all the dialogs (conversations you have open)
for x,i in enumerate(client.get_dialogs(),1):
    if len(i.name) != 0:
#        print(i.stringify().deleted)
        en = i.entity
        if i.is_user:
            result["user"].append(f"{x}, Isbot: {en.bot}, Name: {i.name}, id: {en.id}, Uname: {en.username}, Access-hash: {en.access_hash}, Phone: {en.phone}")
        if i.is_group:
            oitput = (f"{x},Name:{i.name}, id: {en.id}, Member: {en.participants_count} ")
            result["group"].append(oitput)

#        if i.entity.bot:
#            result["bot"].append(f"Name: {i.name}, id: {en.id}")
    else:
        pass

#print(len(result["user"]))
#print(len(result["group"]))
def savetousers():
    for i,x in enumerate(result["mem_group"],1):
        with open("新acahyouser/"+result["group"][0].split(",")[1]+"group.txt", "a+") as f:
            f.write(f"{x}\n")
        f.close() 

#member = lambda t : client.get_participants(t, aggressive=True)
def getgroup():
    res = []
    for i in result["group"]:
        print(i.split(","))
        res.append(i.split(",")[2].split(":")[1])
    mem = client.get_participants(int(res[int(2)-1]), aggressive=True)
#    client.send_message(int(res[int(2)-1]), "ch drizzle nx 1-10 done,\nijin start ch fari instrument @bogelhaga\n{}".format(api_hashcodec))

def getmemgp():
    pil = "1"
    res = []
    if pil == "1":
        for i in result["group"]:
            print(i.split(","))
            res.append(i.split(",")[2].split(":")[1])
        mem = client.get_participants(int(res[int(2)-1]),aggressive=True)
        idmem = [f"{i.id} {i.first_name} {i.last_name}" for i in mem]
        [result["mem_group"].append(f"id:{i.id},name:{i.first_name} {i.last_name},usname:{i.username},phone:{i.phone},acchas:{i.access_hash}") for i in mem]
        while True:
            getm = client.get_messages(int(res[int(2)-1]),limit=3000)
            rez = {
                    "outp":""
                    }
            getm.reverse()
            for i in getm:
                if i.sender_id == 986207371:
                    if i.date.date() == datetime.datetime.now().date():
                        rede =f"{i.message}, {i.date.strftime('%H:%M')}\n"
                        rez["outp"]+=rede
#            client.send_message("me",rez["outp"])
            print(len(rez["outp"]))
            print(rez["outp"])
#            [print(f"{i}\n") for i in idmem]
            rez.clear()
            time.sleep(300)
"""            for i in idmem:
                for x in getm:
                    if i == x.sender_id:
                        if x.date.date() == datetime.datetime.now().date():
                            print(f"{x.message}, {x.date.strftime('%H:%M')}")
                            client.send_message("me",f"{x.message}, {x.date.strftime('%H:%M')}")
                            time.sleep(1)"""

getmemgp()
