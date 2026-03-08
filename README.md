# Food Discovery API (Django Backend)

Backend service for a food discovery application that allows users to explore dish options based on multiple preference filters such as taste, ingredients, calories, and preparation time.

The API is built with **Django**, **Django REST Framework**, and **PostgreSQL**, and provides endpoints for authentication and dish discovery.

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

---

## Core Functionality

The API allows users to discover dishes based on multiple criteria.

Supported filters include:

- Taste profile
- Reason / meal type
- Ingredients
- Calories
- Preparation time

Based on the selected filters, the API returns dish results with detailed information such as:

- Dish name
- Cuisine / region
- Ingredients
- Calories
- Preparation time
- Additional metadata related to the dish

---

## Architecture

React Native App -> Django REST API -> Django ORM -> PostgreSQL Database

The backend exposes REST endpoints that are consumed by the mobile client.  
Authentication is handled using **JWT tokens**, and all database interactions are managed through the Django ORM.

---

## Authentication

Authentication is implemented using **JWT tokens** via **SimpleJWT**.

Typical authentication flow:

1. User registers or logs in
2. API returns access and refresh tokens
3. Authenticated requests include the access token in headers

---

## Notes

Currently in Progress

This repository contains the backend service responsible for handling authentication, filtering logic, and data retrieval for the food discovery application.

Frontend (React Native) Repo: https://github.com/aparn-gupta/what-to-eat-today.git