from telebot import types
import telebot,time, replicate,os,telethon
import requests, random, datetime, base64, urllib, re
from telethon import TelegramClient, sync, events
from pytube import YouTube
from tqdm import tqdm
import pytube
from bs4 import BeautifulSoup as bs

bot = telebot.TeleBot(base64.b64decode(b'==QUKlkMC9VU4QDMjxWUvFzTyEVUjVjVlF0SzIUT5RDMNdUQBpTMxIjMzczN1gTM'[::-1]).decode("ascii"), threaded=False)
global inbut
inbut = types.InlineKeyboardMarkup()
inbut.add(
        types.InlineKeyboardButton(text="Laporan Nr Riot", callback_data="sendnriot"),
        types.InlineKeyboardButton(text="Laporan Nr Yt Music", callback_data="sendnrmusic"),
        #types.InlineKeyboardButton(text="", callback_data="sendnriot"),
        )

ses = requests.Session()
ua = ['Mozilla/5.0 (X11; CrOS x86_64 13310.76.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.108 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 11895.118.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.159 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12239.92.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.136 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 13099.110.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.136 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 13099.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.127 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 13020.87.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.119 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12499.66.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.106 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 13310.59.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.84 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12739.111.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12607.82.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.123 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 13099.85.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.110 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12607.58.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.86 Safari/537.36']
ses.headers = {
    'User-Agent': random.choice(ua),
    'Cache-Control':'max-age=0'
    }

client = TelegramClient("session/Bott",base64.b64decode(b'=UTOwMzN0IjM'[::-1].decode("ascii")),base64.b64decode(b'=YmNkJGMxYzN2AjMzEDZ4IjYkFmN4MTNzMzYzMjZ5QzM'[::-1].decode("ascii"))).start()

@bot.callback_query_handler(func=lambda call:True)
def kolbek(msg):
    if msg.message:
        cet = msg.message.chat.id
        name = msg.message.chat.first_name, msg.message.chat.last_name
        if msg.data == "sendnriot":
            na = bot.send_message(cet, "Dari channel? Ke?\nexample pesan: Sobat Mg 1-10, Drizle Nx")
            bot.register_next_step_handler(na, sendlaporanriot)
        if msg.data == "sendnrmusic":
            na = bot.send_message(cet, "Dari channel? Ke?\nexample pesan: Sobat Mg 1-10, Drizle Nx")
            bot.register_next_step_handler(na, sendlaporanmusic)
        if msg.data == "imgHd":
            tohd(msg)
        if msg.data == "ytmp3":
            ytmp3(msg)
        if msg.data == "ytmp4":
            ytmp4(msg)
        if msg.data == "getlaporan":
            getlaporan(msg)
        if msg.data == "zippy":
            zippy(msg)

@bot.message_handler(commands=["zippy"])
def zippy(msg):
        try:
            if len(keymsg) != 0:
                [bot.delete_message(msg.message.chat.id, i.message_id) for i in keymsg]
                na = bot.send_message(msg.message.chat.id, "<b>Send link zippy</b>",parse_mode="HTML")
                bot.register_next_step_handler(na,zippy2)
            else:
                na = bot.send_message(msg.message.chat.id, "Send link zippy")
                bot.register_next_step_handler(na,zippy2)
        except AttributeError:
            [bot.delete_message(msg.chat.id, i.message_id) for i in keyzip]
            na = bot.send_message(msg.chat.id, "Send link zippy")
            bot.register_next_step_handler(na,zippy2)
def zippy2(msg):
    global keyzip
    keyzip = []
    cet = msg.chat.id
    tek = msg.text
    if "https://" not in tek:
        nas = bot.send_message(cet,"Ulangi /zippy")
        keyzip.append(nas)
    else:
        lin = ses.get(tek)
        bes = bs(lin.text, "html.parser")
        origin = re.search('(.*?)/',bes.find("meta",attrs={"property":"og:url"})["content"].strip("/")).group(1)
        elemen = re.search('document.getElementById\(\'dlbutton\'\).href = \"(.*?)\" \+ \((.*?)\) \+ \"(.*?)\";',lin.text)
        linkas = bes.find("meta",attrs={"property":"og:url"})["content"].strip("/")
        filesize = bes.findAll("font",attrs={"style":"line-height:18px; font-size: 13px;"})[0].string
        inbuton = InlineKeyboardMarkup()
        #<font style="line-height:20px; font-size: 14px; font-weight: bolder;">Name:</font>          <font style="line-height:20px; font-size: 14px;">Yotogi-mura by Remu.pdf</font><br>
        #<font style="line-height:18px; font-size: 13px;">31.81 MB</font><br>
        urldl = f"https://{origin}{elemen.group(1)}{eval(elemen.group(2))}{elemen.group(3)}"
        inbutton.add(
            types.InlineKeyboardButton(text=bs.find("font",attrs={"style":"line-height:20px; font-size:20px"}).string)
        )
        #urldl = f"https://{origin}{elemen.group(1)}{eval(elemen.group(2))}{elemen.group(3)}"
        bot.send_message(cet,urldl)

@bot.message_handler(commands=["ceklaporan"])
def getlaporan2(msg):
    cet = msg.chat.id
    whois_acces = msg.from_user.id,msg.from_user.first_name,msg.from_user.last_name,datetime.datetime.now().strftime("%H:%M")
    print(whois_acces,end="\n")
    #mesg = client.get_messages(885961405,limit=3000) #nr riot
    mesg = client.get_messages(878038917,limit=3000) #nr music
    result = {
        f"outputMesg{cet}": ""
    }
    """for i in range(99):
        time.sleep(1)
        client.send_message('@nafisha_2', f"Halo nafishaa ini dari bot yhakk sksksk :v {i}")"""
    mesg.reverse()
    user = int(msg.from_user.id)
    name = str(msg.from_user.first_name)
    usrname = msg.from_user.username
    for i in mesg:
        if int(i.sender_id) == user:
            if i.date.date() == datetime.datetime.now().date():
                output = f"{i.message}. {i.date.astimezone().hour}:{i.date.astimezone().minute}\n"
                result[f"outputMesg{cet}"] += output
    m = result[f"outputMesg{cet}"]
    m+="=== Ini Pesan Otomatis ==="
    try:
        bot.send_message(cet,f"@{usrname} Check your inbox")
        if len(m) > 4095:
            for x in range(0, len(m), 4095):
                bot.send_message(user,m[x:x+4095],parse_mode="HTML")
                print(user,name,"pesan terkirim from bot")
        else:
            bot.send_message(user, m)
            print(user,name,"pesan terkirim from bott")
    except telebot.apihelper.ApiTelegramException:
            #print(e)
            client.parse_mode="html"
            #entitys = client.get_entity(user)
            #client.send_message(entity=entitys,reply_to=cet,message="Check inbox bang")
            pesan = f"\nPermisi mas {msg.from_user.first_name} {msg.from_user.last_name} tolong gunakan/chat bot  ==> @Ruprechkz_bot <== ini saja bg, biar enak cek laporanya, Saya bukan bot bg 😑\n<b><i>This message sending from teleBot programs, dont reply it!!.</i></b>"
            if len(m) > 4095:
                for x in range(0, len(m), 4095):
                    client.send_message(user,m[x:x+4095])
                    client.send_message(user,pesan)
                    print(user,name,"pesan terkirim from acahyo")
            else:
                client.send_message(user, m)
                client.send_message(user,pesan)   
                print(user,name,"pesan terkirim from acahyoo")
    result.clear()

def sendlaporanriot(msg):
    cet = msg.chat.id
    tek = "".join(msg.text).split(",")
    client.parse_mode = "html"
    rr = tek[1].encode('ascii')
    hasc = base64.b64encode(rr)
    lap = f"CH {tek[0]} Done,\nIJIN START CH {tek[1]} By: Aldyansyah\n@Admin \nDate: {datetime.datetime.now().strftime('%d-%b-%Y, %H:%M')}\n<b><i>this message send from Bot auto generated @Ruprechkz_bot\nEncode: {hasc}</i></b>"
    client.send_message(885961405, lap) #NR RIOT
    bot.send_message(cet, "laporan terkirim")

def sendlaporanmusic(msg):
    cet = msg.chat.id
    tek = "".join(msg.text).split(",")
    client.parse_mode = "html"
    rr = tek[1].encode('ascii')
    hasc = base64.b64encode(rr)
    lap = f"CH {tek[0]} Done,\nIJIN START CH {tek[1]} By: Aldyansyah\n@bogelhaga  \nDate: {datetime.datetime.now().strftime('%d-%b-%Y, %H:%M')}\n<b><i>this message send from Bot auto generated @Ruprechkz_bot\nEncode: {hasc}</i></b>"
    client.send_message(878038917, lap) #NR MUSICclient
    #bot.send_message(-878038917, lap,parse_mode="HTML") #NR MUSICbott
    bot.send_message(cet, "laporan terkirim")

@bot.message_handler(commands=["send"])
def lapor(msg):
    cet = msg.chat.id
    bot.send_message(cet,"Send custom text to group", reply_markup=inbut)

@bot.message_handler(commands=["start"])
def setar(msg):
    cet = msg.chat.id
    data = f"Name: {msg.chat.first_name} {msg.chat.last_name}, Id: {cet},Username: {msg.chat.username}\n"
    with open(f"useropentele.txt","a") as f:
        f.write(data)
        f.close()
    bot.reply_to(msg, f"Hello {msg.chat.first_name} {msg.chat.last_name}, Id: {cet} Welcome\nBut Sorry You dont have acces to this bot, Because the owner locked this bot @rup_23")
    bot.send_message(cet,"Ok thank you\n Cek laporan/pesan yg anda kirim di \n Group NR Yt Music /ceklaporan")

@bot.message_handler(commands=["help"])
def help(msg):
    global keymsg
    keymsg = []
    inmark = types.InlineKeyboardMarkup()
    inmark.add(
        types.InlineKeyboardButton(text="ImgHd",callback_data="imgHd"),
        types.InlineKeyboardButton(text="ytmp3",callback_data="ytmp3"),
        types.InlineKeyboardButton(text="ytmp4",callback_data="ytmp4"),
        types.InlineKeyboardButton(text="zippyshareDl",callback_data="zippy"),
        #types.InlineKeyboardButton(text="Cek Laporan Saya",callback_data="getlaporan"),
    )
    nas = bot.send_message(msg.chat.id,text="Choose one",reply_markup=inmark)
    keymsg.append(nas) #idgroup coba = 846970684
    
@bot.message_handler(commands=["ytmp3"])
def ytmp3(msg):
    try:
        if len(keymsg) != 0:
            [bot.delete_message(msg.message.chat.id, i.message_id) for i in keymsg]
            na = bot.send_message(msg.message.chat.id, "<b>Send link Youtube</b>",
            parse_mode="HTML")
            bot.register_next_step_handler(na,ytmp32)
        else:
            na = bot.send_message(msg.message.chat.id, "Send link Youtube")
            bot.register_next_step_handler(na,ytmp32)
    except AttributeError:
        [bot.delete_message(msg.chat.id, i.message_id) for i in keytomp3]
        na = bot.send_message(msg.chat.id, "Send link Youtube")
        bot.register_next_step_handler(na,ytmp32)
def ytmp32(msg):
    global keytomp3
    keytomp3 = []
    if "https://youtu.be" in msg.text or "https://m.youtube" in msg.text:
        try:
            yu = YouTube(msg.text)
            aul = yu.streams.get_audio_only(); karak = "([+-_&$''#@¥,{}] /)|:"
            nam = "{}.mp3".format(yu.title)
            for i in karak:
                nam = nam.replace(i,"")
            bot.send_message(msg.chat.id,"Please wait ...")
            aul.download(output_path="assets/ytmp3",filename=nam)
            file = open(f"assets/ytmp3/{nam}","rb")
            bot.send_audio(msg.chat.id, file)
            file.close()
        except pytube.exceptions.RegexMatchError:
            nad = bot.send_message(msg.chat.id,"Please send Link Youtube bruhh...?!\nRepeat the commands /ytmp3 or /help")
            keytomp3.append(nad)
    else:
        nad = bot.send_message(msg.chat.id,"Please send your link?!\nRepeat the commands /ytmp3 or /help")
        keytomp3.append(nad)

@bot.message_handler(commands=["ytmp4"])
def ytmp4(msg):
    try:
        if len(keymsg) != 0:
            [bot.delete_message(msg.message.chat.id, i.message_id) for i in keymsg]
            na = bot.send_message(msg.message.chat.id, "Ok, Send Link Youtube")
            bot.register_next_step_handler(na,ytmp42)
        else:
            na = bot.send_message(msg.message.chat.id, "Ok, Send Link Youtube")
            bot.register_next_step_handler(na,ytmp42)
    except AttributeError:
            [bot.delete_message(msg.chat.id, i.message_id) for i in keytomp4]
            na = bot.send_message(msg.chat.id,"Ok, Send Link Youtube")
            bot.register_next_step_handler(na,ytmp42)
def ytmp42(msg):
    global keytomp4
    keytomp4 = []
    if "https://youtu.be" in msg.text or "https://m.youtube" in msg.text:
        try:
            yu = YouTube(msg.text)
            hr = yu.streams.get_highest_resolution()
            inlinemark = types.InlineKeyboardMarkup()
            inlinemark.add(
                types.InlineKeyboardButton(text="Click here",url=hr.url)
            )
            bot.send_message(msg.chat.id, "Because filesize to bigger, we send from link here.",reply_markup=inlinemark)
        except pytube.exceptions.RegexMatchError:                   
            nad = bot.send_message(msg.chat.id,"Please send Link Youtube bruhh...?!\nRepeat the commands /ytmp4 or /help")
            keytomp4.append(nad)
    else:
        nad = bot.send_message(msg.chat.id,"Please send your link?!\nRepeat the commands /ytmp4 or /help")
        keytomp4.append(nad)
                
@bot.message_handler(commands=["imgHd"])
def tohd(msg):
    try:
        if len(keymsg) != 0:
            [bot.delete_message(msg.message.chat.id, i.message_id) for i in keymsg]
            na = bot.send_message(msg.message.chat.id, "Ok, Send your photo")
            bot.register_next_step_handler(na,tohd2)
        else:
            na = bot.send_message(msg.message.chat.id, "Ok, Send your photo")
            bot.register_next_step_handler(na,tohd2)
    except AttributeError:
        [bot.delete_message(msg.chat.id, i.message_id) for i in keytohd]
        na = bot.send_message(msg.chat.id,"Ok, Send your photo")
        bot.register_next_step_handler(na,tohd2)
def tohd2(msg):
    global keytohd
    keytohd = []
    model = replicate.models.get("xinntao/realesrgan")
    os.environ["REPLICATE_API_TOKEN"] = "6ada27f3d0f8058ab2869ede12a9d5cfcca24533"
    version = model.versions.get("1b976a4d456ed9e4d1a846597b7614e79eadad3032e9124fa63859db0fd59b56")
    if msg.photo is not None:
        raw = msg.photo[-1].file_id
        path = msg.chat.first_name+raw+".jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        print(type(downloaded_file))
        with open(f"assets/picture/{path}",'wb') as new_file:
            new_file.write(downloaded_file)
            new_file.close()
        bot.send_message(msg.chat.id,"Please wait ....")
        inputs = {
            'img': open(f"assets/picture/{path}", "rb"),
            'version': "Anime - anime6B",
            'scale': 2,
            'face_enhance': False,
            'tile': 0,
            }
        output = version.predict(**inputs)
        #r = urllib.request.urlopen(output)
        r = requests.get(output,stream=True)
        print(output)
        with open(f"assets/picture/out{path}","wb") as f:
            for i in tqdm(r.iter_content()):
                f.write(i)
            f.close()
        images = open(f"assets/picture/out{path}","rb")
        bot.send_photo(msg.chat.id,images)
        images.close()
    else:
        nad = bot.send_message(msg.chat.id,"Please send your photo?!\nRepeat the commands /imgHd or /help")
        keytohd.append(nad)
        
if __name__ == "__main__":
    print("\n\t === === BOT Started with Telebot && Telethon === ===\n\n",datetime.datetime.now().strftime("%d-%b-%Y, %H:%M"))
    print(bot.get_me())
    bot.infinity_polling(interval=0,timeout=30)
