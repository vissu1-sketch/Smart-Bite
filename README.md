# 🍽️ SmartBite – Digital Restaurant Ordering and Kitchen Management System

## 📌 About the Project
SmartBite is a web-based restaurant ordering and kitchen management application developed using Django and Python. It allows customers to browse food items, add items to a cart, and place orders. Kitchen staff can view incoming orders and update their status through a dedicated kitchen dashboard.

## 🎯 Objectives
- Simplify the restaurant ordering process.
- Display available food items through a digital menu.
- Allow customers to add food items to a cart and place orders.
- Help kitchen staff manage incoming orders.
- Track order progress through different statuses.

## 🛠️ Technologies Used
- **Frontend:** HTML, CSS, JavaScript (if implemented)
- **Backend:** Python, Django
- **Database:** SQLite
- **Development Tool:** Visual Studio Code

## ✨ Key Features
- **Home Page:** Starting page for the application.
- **Digital Menu:** Displays available food items and prices.
- **Shopping Cart:** Allows customers to review selected items.
- **Order Placement:** Submits customer orders.
- **Kitchen Dashboard:** Displays incoming orders for kitchen staff.
- **Order Status Tracking:** Supports the order flow:
  - Pending
  - Preparing
  - Ready
- **Order Tracking:** Allows users to check their order status.

## 🏗️ System Workflow
1. The customer opens the SmartBite website.
2. The customer browses the menu.
3. Selected food items are added to the cart.
4. The customer places an order.
5. The order appears on the kitchen dashboard.
6. Kitchen staff update the order status.
7. The customer can track the order progress.

## ⚙️ Installation and Setup

### Prerequisites
- Python installed on your computer
- Visual Studio Code
- pip package manager

### Step 1: Clone the Repository
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd GenZ_Tab
```

### Step 2: Create a Virtual Environment
```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

**Windows PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install Django
```bash
python -m pip install django
```

### Step 5: Apply Database Migrations
```bash
python manage.py migrate
```

### Step 6: Run the Development Server
```bash
python manage.py runserver
```

### Step 7: Open the Application

Visit the following URL in your browser:

`http://127.0.0.1:8000/`

Kitchen Dashboard:

`http://127.0.0.1:8000/kitchen/`

## 📂 Project Structure
```text
GenZ_Tab/
├── config/
├── restaurant/
│   ├── migrations/
│   ├── templates/
│   │   └── restaurant/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── README.md
```

## 🚀 Future Enhancements
- User authentication for customers and kitchen staff.
- Improved food images and menu presentation.
- Order history and reporting.
- Additional order management features.

## 🎓 Project Purpose
SmartBite was developed as an academic project to demonstrate web development using Django, database integration, digital ordering, and kitchen order management.

## 👩‍💻 Author
**K. Vissu Priya**

---

*SmartBite – Making restaurant ordering and kitchen coordination simpler.*
