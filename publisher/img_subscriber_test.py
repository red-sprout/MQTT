import paho.mqtt.client as mqtt
import base64
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# .env 파일로 별도 관리
BROKER = os.getenv("BROKER")
PORT = int(os.getenv("PORT"))
TOPIC = os.getenv("TOPIC")

# 다운로드 경로
SAVE_DIR = os.path.expanduser("~/Downloads/mqtt_received_images")

os.makedirs(SAVE_DIR, exist_ok=True)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(TOPIC)
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        # print(payload)
        filename, image_data = payload.split(":", 1)
        image_bytes = base64.b64decode(image_data)

        save_path = os.path.join(SAVE_DIR, filename)
        with open(save_path, "wb") as img_file:
            img_file.write(image_bytes)

        print(f"Received and saved image: {save_path}")
    except Exception as e:
        print(f"Error processing message: {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

client.loop_forever()
