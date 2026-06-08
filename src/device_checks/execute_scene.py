# execute_scene.py
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
SCENE_ID = os.environ["SCENE_ID"]

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

def execute_scene():
    url = f"https://api.switch-bot.com/v1.1/scenes/{SCENE_ID}/execute"
    response = requests.post(url, headers=make_headers())
    result = response.json()
    print(f"ステータスコード: {response.status_code}")
    print(f"レスポンス: {result}")

execute_scene()