import paho.mqtt.client as mqtt
import base64
import os
import time

# .env 파일로 별도 관리
BROKER = os.getenv("BROKER")
PORT = os.getenv("PORT")
TOPIC = os.getenv("TOPIC")

# 이미지가 들어있는 상위 디렉토리
IMAGE_DIR = os.path.expanduser("./img/") 

client = mqtt.Client()

def send_images():
    for filename in os.listdir(IMAGE_DIR):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            filepath = os.path.join(IMAGE_DIR, filename)
            with open(filepath, "rb") as img_file:
                image_data = base64.b64encode(img_file.read()).decode("utf-8")

            message = f"{filename}:{image_data}"
            client.publish(TOPIC, message)
            print(f"Sent {filename}")

            time.sleep(1)

client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    send_images()
finally:
    client.loop_stop()
    client.disconnect()
