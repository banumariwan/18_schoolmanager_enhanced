Student Management System
A Django web application for managing student records with authentication and full CRUD operations.

Features
🔐 User Registration & Authentication

👥 Add, View, Update, Delete Students

🔍 Search students by name

🛡️ Secure login-required access

📱 Responsive design

Quick Start
bash
# Clone and setup
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system

# Install dependencies
pip install django

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
Visit http://localhost:8000 and register a new account to start managing students!

Project Structure
students/views.py - Main application logic

students/models.py - Student data model

students/forms.py - Django forms

templates/ - HTML templates

Tech Stack
Django 3.2+

SQLite

HTML/CSS

Django Authentication

