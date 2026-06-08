# Switchbot Automation
Raspberry PI 経由で, Switchbot を遠隔操作する.


## 構成

```
.
├─ src
│   └─ tests                # 動作確認のためのスクリプト
│       ├─ execute_scene.py # switch bot hub のシーンを実行する
│       ├─ get_devices.py   # switch bot のデバイスリストを取得する
│       ├─ get_scenes.py    # switch bot hub のシーンリストを取得する
│       └─ toggle_plug.py   # switch bot plug mini の on/off テスト
├─ .env                     # トークンやデバイスIDなどを記載する環境変数ファイル
├─ .env.example             # これを .env としてRaspberry PIに配置
└─ requirements.txt         # Raspberry PI 側のpythonパッケージ
```

## Raspberry PI Setup

`requirements.txt`を送る.
```bash
# local
scp requirements.txt YOUR_RASPBERRY_PI_ADDRESS:
```

Raspberry PI へ接続し, 
```bash
# local
ssh YOUR_RASPBERRY_PI_ADDRESS
```

仮想環境にパッケージをインストール.
```bash
# raspberry pi
python3 -m venv .venv
source .venv/bin/activate
python -m pip -f requirements.txt
```

スクリプトの転送 & 実行
```bash
# local
scp .env YOUR_RASPBERRY_PI_ADDRESS:
scp -r src YOUR_RASPBERRY_PI_ADDRESS:
```

```bash
# raspberry pi
source .venv/bin/activate
python src/tests/get_devices.py
```

## メモ

- Raspberry PIをシャットダウンするコマンド: `sudo shutdown -h now`