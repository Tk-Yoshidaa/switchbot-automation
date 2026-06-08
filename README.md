# Switchbot Automation
Raspberry PI 経由で, Switchbot を遠隔操作する.


## 構成

```
.
├─ src
│   └─ tests                # 動作確認のためのスクリプト
│       ├─ get_devices.py   # switch bot のデバイスリストを取得する
│       └─ toggle_plug.py   # switch bot plug mini の on/off テスト
├─ .env                     # トークンやデバイスIDなどを記載する環境変数ファイル
├─ .env.example             # これを .env としてRaspberry PIに配置
└─ requirements.txt         # Raspberry PI 側のpythonパッケージ
```

## Raspberry PI Setup

`requirements.txt`を送る.
```
# local
scp requirements.txt YOUR_RASPBERRY_PI_ADDRESS:
```

Raspberry PI へ接続し, 
```
# local
ssh YOUR_RASPBERRY_PI_ADDRESS
```

仮想環境にパッケージをインストール.
```
# raspberry pi
python3 -m venv .venv
source .venv/bin/activate
python -m pip -f requirements.txt
```

スクリプトの転送 & 実行
```
# local
scp -r src YOUR_RASPBERRY_PI_ADDRESS
```

```
# raspberry pi
source .venv/bin/activate
python src/tests/get_devices.py
```