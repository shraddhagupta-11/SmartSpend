# 💰 SmartSpend

SmartSpend is a full-stack personal finance management web application built with Django that helps users track expenses, manage income, plan budgets, monitor savings goals, and gain insights into their financial habits through interactive analytics.

The application is designed to provide a simple and user-friendly experience while demonstrating modern web development practices, authentication systems, database management, financial data visualization, and responsive UI design.

---

## 📖 About the Project

Managing personal finances effectively requires tracking spending patterns, maintaining budgets, and understanding financial behavior over time.

SmartSpend was developed to provide users with a centralized platform where they can:

- Track daily expenses
- Record income sources
- Create and manage budgets
- Set savings goals
- Analyze financial performance
- Visualize spending trends
- Monitor financial progress through dashboards

The project follows a full-stack architecture using Django and SQLite and includes both backend business logic and frontend user interfaces.

---

## ⭐ Key Features

### 🔐 User Authentication

- Secure user registration
- Login and logout functionality
- Session management
- Protected routes and user-specific data

### 💸 Expense Management

- Add expenses
- Edit existing expenses
- Delete expenses
- Categorize spending
- View expense history

### 💵 Income Tracking

- Record multiple income sources
- Monitor monthly income
- Maintain income history

### 📊 Budget Planning

- Create monthly budgets
- Track spending against budgets
- Monitor remaining budget balances

### 🎯 Savings Goals

- Create savings targets
- Track progress toward goals
- Monitor completion percentage

### 📈 Financial Analytics Dashboard

- Summary cards for key financial metrics
- Spending analysis
- Income versus expense tracking
- Budget utilization insights

### 📉 Interactive Charts

- Financial data visualization
- Dynamic charts using Chart.js
- Improved financial decision-making through visual insights

### 👤 Profile Management

- Manage user profile information
- Personalized financial data
- User-specific dashboards

### 📱 Responsive User Interface

- Mobile-friendly design
- Clean dashboard layout
- Optimized user experience across devices

---

## 🛠 Technology Stack

### Backend

- Python
- Django

### Database

- SQLite

### Frontend

- HTML5
- CSS3
- JavaScript

### UI & Visualization

- Bootstrap Icons
- Chart.js

### Development Tools

- Git
- GitHub
- VS Code

---

## 🏗 Project Architecture

```text
SmartSpend/
│
├── accounts/
├── expenses/
├── income/
├── budgets/
├── savings/
├── dashboard/
│
├── templates/
├── static/
│
├── manage.py
├── requirements.txt
└── db.sqlite3
```

### Main Components

| Module | Purpose |
|----------|----------|
| Accounts | Authentication and user management |
| Expenses | Expense tracking functionality |
| Income | Income management |
| Budgets | Budget planning and monitoring |
| Savings | Savings goal tracking |
| Dashboard | Financial analytics and reporting |

---

## 🚀 Installation Guide

### Prerequisites

Install the following before running the project:

- Python 3.10 or newer
- Git
- VS Code (recommended)

---

### Step 1: Clone the Repository

```bash
git clone https://github.com/shraddhagupta-11/SmartSpend.git
```

---

### Step 2: Move into the Project Directory

```bash
cd SmartSpend
```

---

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

---

### Step 4: Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

---

### Step 5: Install Required Packages

```bash
pip install -r requirements.txt
```

---

### Step 6: Apply Database Migrations

```bash
python manage.py migrate
```

---

### Step 7: Create an Admin Account (Optional)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an administrator account.

---

### Step 8: Start the Development Server

```bash
python manage.py runserver
```

---

### Step 9: Open the Application

Visit:

```text
http://127.0.0.1:8000
```

The application should now be running locally.

---

## 📋 Application Workflow

1. Create an account or log in.
2. Add income records.
3. Record daily expenses.
4. Create monthly budgets.
5. Set savings goals.
6. Monitor financial activity through the dashboard.
7. Analyze spending trends using charts and reports.

---

## 🔒 Security Features

- Django authentication system
- Password hashing
- CSRF protection
- Session-based authentication
- User-specific data isolation

---

## 🎯 Learning Outcomes

This project provided hands-on experience with:

- Full-Stack Web Development
- Django Framework
- Authentication Systems
- Database Design
- CRUD Operations
- Financial Data Modeling
- Dashboard Development
- Data Visualization
- Frontend and Backend Integration
- Git and GitHub Workflows

---

