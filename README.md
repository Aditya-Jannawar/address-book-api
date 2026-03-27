# 🚀 Address Book API (FastAPI)

A minimal yet production-ready Address Book API built using **FastAPI**, allowing users to create, update, delete, and search addresses based on geolocation.

---

## 📌 Features

* ✅ Create, Read, Update, Delete (CRUD) operations for addresses
* 📍 Store latitude and longitude for each address
* 🌍 Find nearby addresses within a given radius (in KM)
* 🔍 Input validation using Pydantic
* 🪵 Logging for API operations and error tracking
* ⚙️ Clean architecture with modular structure
* 🔢 API Versioning (`/api/v1/...`)
* 🗄️ SQLite database with SQLAlchemy ORM

---

## 🛠️ Tech Stack

* **FastAPI** – Web framework
* **SQLAlchemy** – ORM
* **SQLite** – Database
* **Pydantic** – Data validation
* **Geopy** – Distance calculation
* **Uvicorn** – ASGI server

---

## 📁 Project Structure

```
app/
 ├── main.py
 ├── api/
 │    └── routes.py
 ├── models/
 │    └── address.py
 ├── schemas/
 │    └── address.py
 ├── services/
 │    └── address_service.py
 ├── db/
 │    ├── database.py
 │    └── base.py
 ├── core/
 │    └── config.py
 └── utils/
      └── logger.py
```

---

## ⚙️ Setup Instructions (Run in under 5 minutes)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Aditya-Jannawar/address-book-api.git
cd address-book-api
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in root:

```
DATABASE_URL=sqlite:///./addresses.db
```

---

### 5️⃣ Run the Application

```bash
uvicorn app.main:app --reload
```

---

## 🌐 API Documentation

Once the server is running:

* Swagger UI 👉 http://127.0.0.1:8000/docs
* ReDoc 👉 http://127.0.0.1:8000/redoc

---

## 📡 API Endpoints

### 📍 Base URL:

```
/api/v1/addresses
```

---

### ➕ Create Address

```
POST /api/v1/addresses
```

### 📄 Get All Addresses

```
GET /api/v1/addresses
```

### 🔍 Get Address by ID

```
GET /api/v1/addresses/{id}
```

### ✏️ Update Address

```
PUT /api/v1/addresses/{id}
```

### ❌ Delete Address

```
DELETE /api/v1/addresses/{id}
```

### 🌍 Get Nearby Addresses

```
GET /api/v1/addresses/nearby?latitude=18.52&longitude=73.85&distance=5
```

---

## 🧠 Design Decisions

* Used **SQLAlchemy ORM** for safe and maintainable DB operations
* Used **Geopy** for accurate geodesic distance calculation
* Applied **input validation at schema level** using Pydantic
* Implemented **logging for traceability and debugging**
* Structured project for **scalability and readability**
* Externalized configuration using `.env`

---

## ⚠️ Notes

* No GUI included (as per assignment)
* API testing can be done via Swagger UI
* SQLite is used for simplicity

---

## 🚀 Future Improvements

* Add Docker support 🐳
* Add unit tests (pytest)
* Add authentication (JWT)
* Add pagination for large datasets

---

## 👨‍💻 Author

Aditya Jannawar
GitHub: https://github.com/Aditya-Jannawar

---
