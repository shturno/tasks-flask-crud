import pytest 
import requests

BASE_URL = 'http://127.0.0.1:5000/'
tasks = []


def test_create_task():
    new_task_data = {
        "name": "Task 1",
        "description": "Task 1 description"
    }
    response = requests.post(BASE_URL + 'tasks', json=new_task_data)
    assert response.status_code == 200


def test_get_tasks():
    response = requests.get(BASE_URL + 'tasks')
    assert response.status_code == 200
    assert "tasks" in response.json()
    assert "total_tasks" in response.json()


def test_get_task():
    response = requests.get(BASE_URL + f'tasks/{tasks[0]["id"]}')
    assert response.status_code == 200
    assert response.json()['id'] == 1


def test_update_task():
    updated_task_data = {
        "name": "Task 1 updated",
        "description": "Task 1 description updated",
        "completed": True
    }
    response = requests.put(BASE_URL + f'tasks/{tasks[0]["id"]}', json=updated_task_data)
    assert response.status_code == 200
    assert response.json()['name'] == updated_task_data['name']
    assert response.json()['description'] == updated_task_data['description']
    assert response.json()['completed'] == updated_task_data['completed']