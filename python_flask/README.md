# Flask App

## Overview

This Flask application demonstrates basic functionality including routing for rendering HTML templates, handling JSON responses, and processing form submissions.

## Installation

Clone the repository:

```sh
git clone <repository_url>
cd <repository_name>
```
# Usage

## Running with Gunicorn (Production Deployment)

Install Gunicorn:

Gunicorn is a Python WSGI HTTP Server for UNIX. Install it using `pip`:

```sh
pip install gunicorn
```
### Run the application with Gunicorn:

From the root directory of your project, run:

```sh
gunicorn -w 4 -b 0.0.0.0:8000 --worker-class=gevent wsgi:app --timeout 60 --log-level debug --log-file=gunicorn.log
```
- -w 4: Number of worker processes (adjust as per your server's capabilities).
- -b 0.0.0.0:8000: Bind address and port number where Gunicorn will listen.
- --worker-class=gevent: Use the gevent worker class for asynchronous processing.
- --timeout 60: Set the worker timeout to 60 seconds.
- --log-level debug: Set the log level to debug.
- --log-file=gunicorn.log: Specify the log file.

### Access the application:

Open a web browser and go to `http://localhost:8000/` to see the application running.

# Running with Flask's Development Server (for testing or local development)

Run the application:

```sh
python app.py
```
The application will start running on`http://localhost:5000/`.

Routes:

- **Home Route: /**

	- Displays a welcome message with a link to the submit page.

- **Submit Route: /submit**

	- Renders a form for submitting a name. On submission, it displays a greeting message.

- **Greet Route: /greet/<name>**

	- Greets the user with a personalized message.

- **JSON Response Route: /api/greet/<name>**

	- Returns a JSON response with a personalized greeting message.

# Structure

- `app.py`: Contains all route definitions and Flask application setup.
- `wsgi.py`: The WSGI entry point.
- `templates/`: Directory containing HTML templates used by the application.

# Dependencies

- Flask: A lightweight WSGI web application framework in Python.
- Gunicorn: A Python WSGI HTTP Server for UNIX.
- Gevent: A coroutine-based Python networking library.

# Notes

This application is configured to run in debug mode (`app.run(debug=True)`) which provides helpful debugging information in case of errors. It is recommended to disable debug mode in production environments.
