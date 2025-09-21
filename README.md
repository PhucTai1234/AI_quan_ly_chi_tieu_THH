# AI_quan_ly
AI Tư vấn Quản lý Chi tiêu qua SMS
Dự án AI Tư vấn Quản lý Chi tiêu qua SMS là một ứng dụng microservices sử dụng trí tuệ nhân tạo để hỗ trợ người dùng theo dõi chi tiêu qua tin nhắn SMS.
Tính năng
- Nhận tin nhắn SMS mô phỏng và phân tích yêu cầu ("Chi tieu").
- Tính toán chi tiêu dựa trên dữ liệu từ MongoDB.
- Gửi phản hồi chi tiêu (ví dụ: "Bạn đã tiêu 2,000,000đ/3,000,000đ").
- Cảnh báo gia đình nếu chi tiêu vượt 80% ngân sách.Công nghệ sử dụng
- **Backend**: FastAPI, Python 3.8
- **Database**: MongoDB
- **Message Queue**: RabbitMQ
- **Containerization**: Docker, Docker Compose
- **AI**: Sử dụng PhoBERT (NLP) và Scikit-learn (phân tích)

Yêu cầu hệ thống

Hệ điều hành: Windows 10/11 (hoặc tương thích Docker).
Docker: Phiên bản mới nhất (tải từ docker.com).
Docker Compose: Đi kèm với Docker Desktop.
PowerShell: Đã tích hợp sẵn trên Windows.

Cài đặt và chuẩn bị

Yêu cầu: Python 3.8+, Docker.
Cài đặt:

Cài Python: python -m ensurepip --upgrade và python -m pip install --upgrade pip.
Tạo môi trường ảo: python -m venv venv và kích hoạt (source venv/bin/activate trên Linux/Mac, venv\Scripts\activate trên Windows).
Cài thư viện: pip install fastapi uvicorn pymongo pika.

Chạy MongoDB và RabbitMQ: docker-compose up --build
