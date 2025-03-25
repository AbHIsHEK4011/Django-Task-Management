# Django Task Management API

This is a **Task Management API** built using **Django** and **Django REST Framework (DRF)**. The API allows users to **create tasks, assign tasks to users, and retrieve assigned tasks**.

---

## **📌 Features**
- User authentication using **JWT (JSON Web Token)**.
- Create, update, and delete tasks.
- Assign tasks to multiple users.
- Retrieve tasks assigned to a specific user.

---

## **📂 Project Setup**

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-repo/task-management-api.git
cd task_management
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Apply Database Migrations**
```sh
python manage.py migrate
```

### **5️⃣ Create a Superuser (Admin User)**
```sh
python manage.py createsuperuser
```
Enter **username, email, and password** when prompted.

### **6️⃣ Run the Development Server**
```sh
python manage.py runserver
```
Server will start at: `http://127.0.0.1:8000/`

---

## **🔐 Authentication (JWT)**

### **1️⃣ Obtain Access Token**
- **Endpoint:** `POST /api/token/`
- **Request Body:**
  ```json
  {
    "username": "admin",
    "password": "adminpassword"
  }
  ```
- **Response:**
  ```json
  {
    "access": "your-access-token",
    "refresh": "your-refresh-token"
  }
  ```

### **2️⃣ Use the Token in Requests**
Add the following header to authenticate:
```json
{
  "Authorization": "Bearer your-access-token"
}
```

### **3️⃣ Refresh Token**
- **Endpoint:** `POST /api/token/refresh/`
- **Request Body:**
  ```json
  {
    "refresh": "your-refresh-token"
  }
  ```

---

## **📌 API Endpoints**

### **1️⃣ Create a Task**
- **Endpoint:** `POST /api/tasks/`
- **Headers:**
  ```json
  {
    "Authorization": "Bearer your-access-token",
    "Content-Type": "application/json"
  }
  ```
- **Request Body:**
  ```json
  {
    "name": "Fix Bug in App",
    "description": "Resolve issue in authentication module",
    "task_type": "Bug Fix",
    "status": "pending"
  }
  ```

### **2️⃣ Assign Task to Users**
- **Endpoint:** `POST /api/assign_task/`
- **Request Body:**
  ```json
  {
    "task_id": 1,
    "user_ids": [2, 3]
  }
  ```

### **3️⃣ Get Tasks for a Specific User**
- **Endpoint:** `GET /api/users/{user_id}/tasks/`

### **4️⃣ Update Task**
- **Endpoint:** `PATCH /api/tasks/{task_id}/`
- **Request Body:**
  ```json
  {
    "status": "completed"
  }
  ```

### **5️⃣ Delete a Task**
- **Endpoint:** `DELETE /api/tasks/{task_id}/`

---


## **📞 Support**
If you have any questions, feel free to open an issue in the repository!
