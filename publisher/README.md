# MQTT Publisher(Python)

## 디렉토리 구조

```bash
./publisher/
    ├── .env
    ├── img_publisher.py # 이미지를 base64로 변환 후 전송
    ├── img_subscriber_test.py
    └── img/
        └── test.png
```

## .env 예시

```env
BROKER = "localhost"
PORT = 1883
TOPIC = "image/upload"
```