# 🚚 Smart Delivery Management System

https://smart-delivery-system-override.onrender.com/

**Mirai Courier.co – Scalable Delivery Platform**

---

## 📌 Project Overview

Mirai Courier.co is a rapidly growing local delivery company operating across the **Klang Valley**. Due to increased demand from online platforms, the existing delivery system faced **scalability, performance, and reliability issues**.

This project introduces a **cloud-based, scalable delivery management system** that improves system performance, database efficiency, and operational transparency for **customers, administrators, and riders**.

---

## 🎯 Project Objectives

* Expand system scalability to support high traffic
* Eliminate single-server bottlenecks
* Improve and normalize database design
* Enable real-time order tracking
* Allow riders to update delivery status independently

---

## ❌ Problems in Existing System

* System slows down during peak usage
* Single-server architecture causes crashes
* Poor database design leads to bottlenecks
* Admin cannot efficiently monitor high-volume orders
* Riders cannot update delivery status
* Delayed communication between system roles

---

## ✅ Solutions Implemented

* RESTful API-based architecture using Flask
* Cloud deployment with separated app and database servers
* Optimized PostgreSQL relational database
* Role-based system (Customer, Admin, Rider)
* Order lifecycle management:

  `Pending → Assigned → On Delivery → Completed`

---

## 🧱 System Architecture

```
Customer / Admin / Rider
        ↓
     Flask API
        ↓
  PostgreSQL Database
```

The system uses a **stateless API architecture**, enabling better scalability and reliability under heavy traffic.

---

## 👥 User Roles & Features

### 🧑 Customer

* View products
* Place orders
* Track order status

### 🧑‍💼 Admin

* View all orders
* Assign riders
* Monitor delivery status
* Delete/manage orders

### 🏍️ Rider

* View assigned orders
* Start delivery
* Complete delivery
* Update order status

---

## 🗄️ Database Design

### Core Tables

* `customers`
* `orders`
* `order_items`
* `products`
* `riders`

### Design Highlights

* Normalized schema
* Foreign key constraints
* Indexed primary keys
* ACID-compliant transactions

---

## 🛠️ Technology Stack

### Backend

* Python
* Flask
* psycopg2

### Database

* PostgreSQL

### Frontend

* HTML
* Bootstrap

### Deployment & Tools

* Render (Cloud Hosting)
* Render PostgreSQL
* Git & GitHub
* VS Code

---

## ☁️ Infrastructure & Significance

| Component              | Significance                          |
| ---------------------- | ------------------------------------- |
| Flask API Server       | Handles business logic and routing    |
| PostgreSQL Server      | Stores structured and normalized data |
| Cloud Hosting (Render) | Improves scalability and availability |
| GitHub                 | Version control and collaboration     |
| HTTPS                  | Secure communication                  |

---

## 📂 Project Structure

```
Smart-Delivery/
│
├── app/
│   ├── __init__.py
│   ├── dao.py
│   └── templates/
│       ├── order.html
│       ├── admin.html
│       ├── rider.html
│       ├── login.html
│       └── track.html
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/smart-delivery.git
cd smart-delivery
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
python main.py
```

Access URLs:

* Customer: `/order`
* Admin: `/admin`
* Rider: `/rider/<rider_id>`

---

## 🔐 Admin Login

```
Username: admin
Password: admin123
```

---

## 📈 Future Enhancements

* Load balancer & horizontal scaling
* Real-time notifications
* JWT authentication
* Payment gateway integration
* Mobile rider application
* Analytics dashboard

---

## 📚 SDLC Methodology

This project follows the **System Development Life Cycle (SDLC)**:

1. Requirement Analysis
2. System Design
3. Implementation
4. Testing
5. Deployment
6. Maintenance

---

## 📜 License

Developed for **academic purposes** under Mirai Courier.co case study.
