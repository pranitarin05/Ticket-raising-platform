A backend REST API built using Django and Django REST Framework for managing campus issue tickets. Students can raise tickets and administrators can manage them efficiently.

🚀 Project Overview

The Smart Campus Helpdesk system allows:

Students to create and track issues

Administrators to manage and update ticket status

Secure authentication using JWT

Advanced filtering, ordering, searching, and pagination

This project demonstrates backend concepts like:

CRUD operations

JWT Authentication

PostgreSQL integration

Filtering & Searching

Pagination

Clean API design

🛠 Tech Stack

Python

Django

Django REST Framework

PostgreSQL

Simple JWT Authentication

Django Filter

📂 Project Structure smart_campus/ │ ├── smart_campus/ # Project settings ├── tickets/ # Ticket app │ ├── models.py │ ├── serializers.py │ ├── views.py │ ├── urls.py │ ├── manage.py └── README.md 🗄 Database

PostgreSQL is used as the primary database.

Ticket Model Fields

id

title

description

category (classroom / hostel / network)

priority (low / medium / high)

status (open / in-progress / closed)

created_by (User)

created_at

updated_at

🔐 Authentication

JWT-based authentication is implemented using djangorestframework-simplejwt.

Authentication Flow

User logs in using username & password.

Access and refresh tokens are generated.
