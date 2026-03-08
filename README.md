# Food Discovery API (Django Backend)

Backend service for a food discovery application that allows users to explore dish options based on multiple preference filters such as taste, origin, ingredients, cooking_method, calories, and preparation time.


---

## Tech Stack

- **Django**
- **Django REST Framework**
- **PostgreSQL**
- **Django ORM**
- **JWT Authentication (SimpleJWT)**

---

## Features

- REST API for food discovery
- Filter-based dish search
- JWT authentication using SimpleJWT
- Secure user registration and login
- Structured relational data using PostgreSQL
- Query handling using Django ORM

--

Based on the selected filters, the API returns relevant dish results with detailed information along with its recipe.


---

## Architecture

React Native App -> Django REST API -> Django ORM -> PostgreSQL Database

The backend exposes REST endpoints that are consumed by the mobile client.  
Authentication is handled using **JWT tokens**, and all database interactions are managed through the Django ORM.

---



## Notes

Currently in Progress


Frontend (React Native) Repo: https://github.com/aparn-gupta/what-to-eat-today.git