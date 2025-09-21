from fastapi import FastAPI
from pymongo import MongoClient
import pika
import json

app = FastAPI()
client = MongoClient("mongodb://localhost:27017/")
db = client["finance_db"]
users = db["users"]

# Thêm dữ liệu mẫu
users.insert_one({"phone": "+84987654321", "budget": 3000000, "spent": 2000000})

def send_to_notification(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='notifications')
    channel.basic_publish(exchange='', routing_key='notifications', body=json.dumps(message).encode())
    connection.close()
    print(f"Cảnh báo gửi đến gia đình: {message}")

@app.post("/analyze")
async def analyze(data: dict):
    message = data.get("message")
    phone = data.get("phone")
    user = users.find_one({"phone": phone})
    
    if "chi tieu" in message.lower():
        response = f"Bạn đã tiêu {user['spent']:,}đ/{user['budget']:,}đ."
        if user["spent"] > user["budget"] * 0.8:  # Cảnh báo nếu vượt 80% ngân sách
            send_to_notification({"phone": phone, "alert": f"{phone} tiêu {user['spent']:,}đ vượt ngân sách!"})
        print(f"Phản hồi cho {phone}: {response}")
        return {"response": response}
    return {"response": "Vui lòng gửi 'Chi tieu' để kiểm tra."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)