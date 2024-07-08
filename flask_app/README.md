# Flask Application with PostgreSQL

This project is a simple Flask application that connects to a PostgreSQL database. It includes a Docker setup to simplify the development and deployment process.

## Prerequisites
Ensure you have the following installed on your machine:

- Docker
- Docker Compose

## Steps
Clone the repository:

```sh
git clone https://github.com/yourusername/flask_app.git
cd flask_app
```
Build and start the Docker containers:

```sh
docker-compose up --build
```
## Usage

Once the containers are up and running, the Flask application will be accessible at `http://localhost:5000`.

To stop the application, press `CTRL+C` in the terminal where `docker-compose` up is running.

## Accessing the Database
To access the PostgreSQL database:

Open a new terminal.

Run the following command to open a bash session inside the PostgreSQL container:

```sh
docker exec -it flask_app_db_1 bash
```
Connect to the PostgreSQL database using psql:

```sh
psql -U postgres -d flaskdb
```
## Endpoints

- GET /: Returns a welcome message.
- GET /users: Retrieves a list of users.
- POST /users: Creates a new user.
- GET /posts: Retrieves a list of posts.
- POST /posts: Creates a new post.
