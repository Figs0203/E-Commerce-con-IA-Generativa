# E-Commerce Platform with AI-Generative Features

## Description
This project is an **AI-powered e-commerce platform** built with Django that revolutionizes how sellers create product listings. Instead of manually writing descriptions and labels, sellers can simply upload a product photo, and our AI system will automatically:

- **Generate detailed product descriptions** automatically
- **Suggest relevant product labels and tags** 
- **Identify product categories** based on visual content
- **Automate tedious listing creation** to save sellers hours of work

The platform provides a complete MVP with user authentication, AI-powered product management, and intelligent search capabilities.

---

## Project Status
**Currently in active development** with a **fully functional MVP** that includes:
- Complete user authentication system
- Product CRUD operations (Create, Read, Update, Delete)
- Image upload and management
- Product search and filtering
- Category-based organization
- Admin interface for content management
- **AI Integration in Progress**: Computer vision and description generation

---

## Current Technology Stack
- **Backend**: Django 5.2.4 (Python web framework)
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Image Processing**: Pillow 11.3.0
- **AI/ML**: Computer vision and natural language processing (in development)
- **Frontend**: Django Templates with Bootstrap styling
- **Authentication**: Django's built-in user system
- **Version Control**: Git + GitHub

---

## Features

### **Implemented Features**
- **User Management**: Registration, login, logout, and authentication
- **Product Management**: Create, edit, delete, and publish products
- **Image Handling**: Upload and display product images
- **Search & Filter**: Search by title, filter by category and price range
- **Category System**: Organized product categorization
- **Admin Panel**: Django admin interface for content management
- **Responsive Design**: Bootstrap-based responsive UI

### **Core Value Proposition**
This platform solves the **#1 pain point** for online sellers: **creating detailed product listings is time-consuming and tedious**. Our AI solution:
- **Reduces listing creation time** from 15-30 minutes to 2-3 minutes
- **Improves listing quality** with AI-generated descriptions and labels
- **Increases conversion rates** through better product presentation
- **Eliminates writer's block** when describing products

### **AI-Powered Features (Core Innovation)**
- ** Computer Vision Analysis**: Automatically analyze product images
- ** Smart Description Generation**: AI creates detailed product descriptions from photos
- ** Automatic Labeling**: Generate relevant tags and labels based on visual content
- ** Intelligent Categorization**: AI suggests product categories from image analysis
- ** Listing Automation**: Transform photo uploads into complete product listings
- ** Content Optimization**: AI-enhanced product descriptions for better conversions

---

##  Quick Start Guide
> **Note:** This guide assumes basic familiarity with Python and Django.  
> If you are new to Django, you can still follow along — each step is explained clearly.

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### 1. **Clone the Repository**
```bash
git clone <Repository-url>
cd E-Commerce-con-IA-Generativa
```

### 2. **Set Up Virtual Environment**
```bash
# Windows
python -m venv env
env\Scripts\activate

# macOS/Linux
python3 -m venv env
source env/bin/activate
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 5. **Make Migrations**
```bash
python manage.py makemigrations
```

### 6. **Apply Database Migrations**
```bash
python manage.py migrate
```

### 7. **Set Up Default Categories**
```bash
python manage.py setup_categories
```


### 8. **Run Development Server**
```bash
python manage.py runserver
```

### 9. **Access the Platform**
- **Main Site**: [http://localhost:8000](http://localhost:8000)
- **Admin Panel**: [http://localhost:8000/admin](http://localhost:8000/admin)


**Note**: This is a Django-based **AI-powered e-commerce platform** that revolutionizes product listing creation. The AI features are the core innovation that sets this platform apart from traditional e-commerce solutions. This is not just another marketplace - it's an intelligent tool that automates the most tedious part of selling online.
