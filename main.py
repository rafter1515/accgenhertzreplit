import hmac
import base64
from hashlib import sha1
import os
import secmail
from time import sleep
def generate_device_Id():
    devicee = requests.get("https://ed-generators.herokuapp.com/device")
    return devicee.text

import aminofix as amino
import json
import threading
import wget
import requests
import heroku3
from new import sid, emaill, passwordd, custompwd, chatlink, private, key, app_name, deviceid, nickname, replit
from bs4 import BeautifulSoup

def restart():
    heroku_conn = heroku3.from_key(key)
    botapp = heroku_conn.apps()[app_name]
    botapp.restart()


client = amino.Client(deviceId=deviceid)
#client.login(emaill, passwordd)
client.login_sid(SID=sid)
bb = client.get_from_code(chatlink)
chatId = bb.objectId
cid = bb.comId
client.join_community(cid)
sub = amino.SubClient(comId=cid, profile=client.profile)
sub.join_chat(chatId)


def find():
    while True:
        p = sub.get_chat_messages(chatId=chatId, size=1).content
        # print(p)
        for j in p:
            g = j
        # print(g)
        l = f"{g}"
        length = str(len(l))
        if "6" == length:
            break
    return g

def gen_email():
    mail = secmail.SecMail()
    email = mail.generate_email()
    return email

def get_message(email):
    url="0"
    try:
        sleep(3)
        f=email
        mail = secmail.SecMail()
        inbox = mail.get_messages(f)
        print('done')
        for Id in inbox.id:
          msg = mail.read_message(email=f, id=Id).htmlBody
          bs = BeautifulSoup(msg, 'html.parser')
          images = bs.find_all('a')[0]
          url = (images['href']+'\n')
          if url is not None:
            print('Vrification Url\n')
            print(url)
    except:
        pass
    return url

password = custompwd
# client.devicee()
de = generate_device_Id()
client = amino.Client(de)
for _ in range(3):
    try:
        os.remove("code.png")
    except:
        pass
    dev = client.device_id
    email = gen_email()
    print(email)
    client.request_verify_code(email=email)
    link = get_message(email)

    wget.download(url=link, out="code.png")
    with open("code.png", "rb") as file:
        sub.send_message(chatId=chatId, fileType="image", file=file)
    p = sub.get_chat_messages(chatId=chatId, size=1).content
    code = find()

    try:
        client.register(email=email, password=password, nickname=nickname, verificationCode=code, deviceId=dev)
        d = {}
        d["email"] = str(email)
        d["password"] = str(password)
        d["device"] = str(dev)
        # t=json.dumps(d)
        print(d)
        requests.get(url=f"{replit}/api/save?email={str(email)}&password={str(password)}&device={str(dev)}")
    except Exception as l:
        print(l)
        pass

    # de=client.devicee()
de = generate_device_Id()
client = amino.Client(de)
for _ in range(2):
    try:
        os.remove("code.png")
    except:
        pass
    dev = client.device_id
    email = gen_email()
    print(email)
    client.request_verify_code(email=email)
    link = get_message(email)
    wget.download(url=link, out="code.png")
    with open("code.png", "rb") as file:
        sub.send_message(chatId=chatId, fileType="image", file=file)
    code = find()

    try:
        client.register(email=email, password=password, nickname=nickname, verificationCode=code, deviceId=dev)
        d = {}
        d["email"] = str(email)
        d["password"] = str(password)
        d["device"] = str(dev)
        # t=json.dumps(d)
        print(d)
        requests.get(url=f"{replit}/api/save?email={str(email)}&password={str(password)}&device={str(dev)}")
    except Exception as k:
        print(k)
        pass

restart()
