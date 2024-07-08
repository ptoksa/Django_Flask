# Flask and MariaDB Docker Project

This project sets up a Flask web application with a MariaDB database using Docker.

## Table of Contents
- [Flask and MariaDB Docker Project](#flask-and-mariadb-docker-project)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Project Structure](#project-structure)
    - [Description of Files](#description-of-files)
  - [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
  - [Interacting with the Database](#interacting-with-the-database)
- [Stopping the Application](#stopping-the-application)

## Prerequisites

Make sure you have the following installed:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Project Structure
```plaintext
flask_mariadb_docker/
│
├── app/
│ ├── init.py
│ ├── app.py
│ ├── config.py
│ └── requirements.txt
│
├── init_db.sql
├── Dockerfile
├── docker-compose.yml
└── README.md
```
### Description of Files
- `app/`: Directory containing the Flask application code.
- `app/app.py`: Main Flask application file.
- `app/config.py`: Configuration file for Flask.
- `app/requirements.txt`: Python dependencies for the Flask application.
- `init_db.sql`: SQL script to initialize the database.
- `Dockerfile`: Dockerfile to build the Flask application container.
- `docker-compose.yml`: Docker Compose file to define and run multi-container Docker applications.

## Setup and Installation

1. **Clone the repository:**

```sh
git clone https://github.com/yourusername/flask_mariadb_docker.git
cd flask_mariadb_docker
```
2. **Initialize and start the containers:**

```sh
docker-compose up --build
```
3. **Initialize the database:**

Open a new terminal window and execute the SQL script:

```sh
docker exec -i mariadb_container mariadb -uflaskuser -pflaskpassword flaskdb < init_db.sql
```
# Running the Application

After running `docker-compose up --build`, the Flask application will be accessible at:

```sh
http://localhost:5000
```
## Interacting with the Database

Access the MariaDB container:

```sh
docker exec -it mariadb_container mariadb -uflaskuser -pflaskpassword flaskdb
```
Basic SQL Commands:

- Show tables:

```sh
SHOW TABLES;
```
- Describe table structure:

```sh
DESCRIBE users;
```
- Insert data:

```sh
INSERT INTO users (username, email) VALUES ('john_doe', 'john@example.com');
INSERT INTO users (username, email) VALUES ('jane_doe', 'jane@example.com');
```
- Query data:

```sh
SELECT * FROM users;
```
# Stopping the Application

Stop the containers:

```sh
docker-compose down
```
