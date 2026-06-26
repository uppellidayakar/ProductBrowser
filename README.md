
# Product Browser Backend

## Overview

This project is a Django REST Framework backend developed as part of the **CodeVector Internship Take-Home Assignment**.

The application provides a scalable REST API for browsing approximately **200,000 products** with efficient pagination and category filtering. It is designed to perform well on large datasets while maintaining consistent pagination even when new products are added.

---

# Features

* Browse 200,000 products
* Products displayed in **newest-first** order
* Filter products by category
* Cursor-based pagination for stable navigation
* Bulk data generation using Django Management Command
* MySQL database
* Optimized database queries

---

# Tech Stack

* Python 3
* Django
* Django REST Framework
* MySQL

---

# Project Structure

```
product_browser/
│
├── config/
├── products/
│   ├── management/
│   │   └── commands/
│   │       └── seed_products.py
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── pagination.py
│   ├── views.py
│   ├── urls.py
│
├── requirements.txt
├── README.md
└── manage.py
```

---

# Database Schema

Each product contains:

* id
* name
* category
* price
* created_at
* updated_at

Indexes are used to improve filtering and ordering performance.

---

# API Endpoints

## List Products

```
GET /api/products/
```

Returns products ordered by newest first.

---

## Filter by Category

```
GET /api/products/?category=Electronics
```

Available categories:

* Electronics
* Books
* Clothing
* Home
* Sports
* Beauty

---

## Pagination

Cursor Pagination is implemented.

Example:

```
GET /api/products/?cursor=<cursor_value>
```

---

# Data Generation

A custom Django Management Command generates approximately **200,000 products**.

Generation uses Django's `bulk_create()` with batches of **5000 records**, making the insertion process significantly faster than inserting one record at a time.

Run:

```bash
python manage.py seed_products
```

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project:

```bash
cd <project-folder>
```

Create a virtual environment:

```bash
python -m venv env
```

Activate the virtual environment:

### Windows

```bash
env\Scripts\activate
```

### Linux / macOS

```bash
source env/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Generate sample data:

```bash
python manage.py seed_products
```

Run the development server:

```bash
python manage.py runserver
```

---

# Design Decisions

### Why MySQL?

MySQL is a reliable relational database with strong indexing support and excellent performance for structured data.

---

### Why Cursor Pagination?

Cursor Pagination was chosen instead of offset/page-number pagination because it provides stable pagination while the dataset is changing.

If new products are inserted while users browse the catalog, Cursor Pagination prevents duplicate or skipped records.

---

### Why bulk_create()?

Generating 200,000 records individually would require 200,000 insert queries.

Using `bulk_create()` significantly reduces database operations by inserting records in batches.

---

### Query Optimization

The API fetches only the required fields using Django ORM's `only()` method and orders results by:

* `created_at` (descending)
* `id` (descending)

This provides deterministic ordering for cursor pagination.

---

# Future Improvements

Given additional development time, the following enhancements could be added:

* Product search
* Sorting by price
* Authentication & Authorization
* OpenAPI / Swagger documentation
* Docker support
* Unit and integration tests
* Redis caching
* CI/CD pipeline

---

# AI Usage

AI tools were used as a learning and productivity aid to:

* Discuss architecture decisions
* Review Django REST Framework implementation
* Improve code readability
* Generate documentation
* Validate best practices

All code was reviewed, understood, tested, and modified before submission.

---

# Author

**Uppelli Dayakar**

Backend Developer (Python | Django | MySQL)


# Adding New Product like this at the new shell
from products.models import Product
from django.utils import timezone

Product.objects.create(
    name="New Product",
    category="Electronics",
    price=999.99,
    created_at=timezone.now(),
    updated_at=timezone.now()
 )