from fastapi import FastAPI
import pika
import json
import time

app = FastAPI()

def callback(ch, method, properties, body):
    data = json.loads(body.decode())
    phone = data.get("phone")
    response = data.get("response")
    print(f"Gửi SMS mô phỏng đến {phone}: {response}")

def receive_from_ai():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='responses')
    channel.basic_consume(queue='responses', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

@app.post("/receive_sms")
async def receive_sms(data: dict):
    message = data.get("Body")
    phone = data.get("From")
    print(f"Nhận tin nhắn từ {phone}: {message}")
    
    # Gửi tin nhắn đến AI Service qua RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='requests')
    channel.basic_publish(exchange='', routing_key='requests', body=json.dumps({"message": message, "phone": phone}).encode())
    connection.close()
    
    # Chờ phản hồi (mô phỏng)
    time.sleep(1)
    return {"status": "Processed"}

# Chạy nhận tin nhắn từ AI
import threading
threading.Thread(target=receive_from_ai, daemon=True).start()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)