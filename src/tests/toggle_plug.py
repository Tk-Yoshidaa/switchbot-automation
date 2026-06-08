# toggle_plug.py
import time
import hmac
import hashlib
import base64
import uuid
import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["SWITCHBOT_TOKEN"]
SECRET = os.environ["SWITCHBOT_SECRET"]
BOT_DEVICE_ID = os.environ["BOT_DEVICE_ID"]


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

def set_plug(turn_on: bool):
    command = "turnOn" if turn_on else "turnOff"
    url = f"https://api.switch-bot.com/v1.1/devices/{BOT_DEVICE_ID}/commands"
    payload = {
        "command": command,
        "parameter": "default",
        "commandType": "command"
    }
    response = requests.post(url, json=payload, headers=make_headers())
    result = response.json()
    print(f"コマンド: {command}")
    print(f"ステータス: {response.status_code}")
    print(f"レスポンス: {result}")

def get_plug_status():
    url = f"https://api.switch-bot.com/v1.1/devices/{BOT_DEVICE_ID}/status"
    response = requests.get(url, headers=make_headers())
    result = response.json()
    power = result["body"]["power"]
    print(f"現在の状態: {power}")
    return power

set_plug(True)   # オン
time.sleep(3)
get_plug_status()
set_plug(False)  # オフ