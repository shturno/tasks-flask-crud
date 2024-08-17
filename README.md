# Task Manager API

## Introduction

The Task Manager API is a simple RESTful API built with Flask to manage tasks. It allows you to create, read, update, and delete tasks, providing a basic structure for managing a to-do list. This project can serve as a foundation for more complex task management applications.

## Features

- Create a new task
- List all tasks
- Get details of a specific task
- Update a task
- Delete a task

## Prerequisites
Make sure you have the following installed on your system:

- Python 3.x
- pip (Python package installer)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/task-manager-api.git
   cd task-manager-api```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**

   ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

   ```bash
   python app.py
   ```

5. **Access the API:**

   Open your web browser and go to `http://localhost:5000/` to access the API.

## API Endpoints
The following endpoints are available:

- Create a Task
URL: /tasks
Method: POST
Request Body: { "title": "Task Title", "description": "Task Description" }
Response: {
  "message": "New task created", "task": {"id": 1, "name": "Task name", "description": "Task description", "completed": false}
}

- List all Tasks
URL: /tasks
Method: GET
Response: {"tasks": [{"id": 1, "name": "Task name", "description": "Task description", "completed": false}],"total_tasks": 1
}

- Get Task Details
URL: /tasks/<int:task_id>
Method: GET
Response: {"id": 1, "name": "Task name", "description": "Task description", "completed": false}

- Update a Task
URL: /tasks/<int:task_id>
Method: PUT
Request Body: { "title": "Updated Task Title", "description": "Updated Task Description" }
Response: {"message": "Task updated", "task": {"id": 1, "name": "Updated Task name", "description": "Updated Task description", "completed": false}
}

- Delete a Task
URL: /tasks/<int:task_id>
Method: DELETE
Response: {"message": "Task deleted"}

## Dependencies
The following dependencies are used in this project:

- Flask: A micro web framework for Python (3.0.3)
- Flask-SQLAlchemy: An extension for Flask that adds support for SQLAlchemy (3.1.1)
- Flask-Cors: An extension for Flask that adds support for Cross-Origin Resource Sharing (3.0.10)
- Werkzeug: A utility library for WSGI web applications (2.3.0)

## Author
Gabriela Alvarenga.