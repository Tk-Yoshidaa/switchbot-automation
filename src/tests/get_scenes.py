# get_scenes.py
import os
import time
import hmac
import hashlib
import base64
import uuid
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["SWITCHBOT_TOKEN"]
SECRET = os.environ["SWITCHBOT_SECRET"]

def make_headers():
    nonce = str(uuid.uuid4())
    t = str(int(round(time.time() * 1000)))
    string_to_sign = TOKEN + t + nonce
    sign = base64.b64encode(
        hmac.new(
            SECRET.encode("utf-8"),
            msg=string_to_sign.encode("utf-8"),
            digestmod=hashlib.sha256
        ).digest()
    ).decode("utf-8")
    return {
        "Authorization": TOKEN,
        "Content-Type": "application/json",
        "sign": sign,
        "nonce": nonce,
        "t": t,
    }

def get_scenes():
    url = "https://api.switch-bot.com/v1.1/scenes"
    response = requests.get(url, headers=make_headers())
    data = response.json()
    for scene in data["body"]:
        print(f"名前: {scene['sceneName']}")
        print(f"ID:   {scene['sceneId']}")
        print("---")

get_scenes()