# MyBlog Django Project

MyBlog is a web application built using Django, allowing users to create and manage blog posts. This README provides an overview of the project structure, setup instructions, and basic usage.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Features

- User authentication and authorization using Django's built-in authentication system.
- CRUD functionality for managing blog posts (Create, Read, Update, Delete).
- Admin interface for managing users, posts, and other administrative tasks.
- Docker setup for easy deployment with MySQL database.
- Integration with Bootstrap for responsive design.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your local machine.
- Docker installed (optional, for running MySQL container).
- Git installed for version control.

## Installation

#### Clone the repository:

```sh
git clone <repository-url>
cd myblog
```
#### If using Docker for MySQL:

- Install Docker and Docker Compose.
- Start MySQL container:

```sh
docker-compose up -d
```
#### Apply migrations to create database tables:

```sh
python manage.py migrate
```
#### Set up Django superuser (admin user):

```sh
python manage.py createsuperuser
```
Follow the prompts to create a superuser account.

# Usage

#### Start the development server:

```sh
python manage.py runserver
```
The application will be accessible at `http://localhost:8000`.

Access the Django admin interface:

Navigate to `http://localhost:8000/admin/` and log in with the superuser credentials created earlier.

Create, update, delete blog posts via the admin interface or test the public-facing blog features.
