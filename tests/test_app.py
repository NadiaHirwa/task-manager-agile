import os
import pytest
import app as app_module
import models

@pytest.fixture
def client(monkeypatch):
    test_db = "test_tasks.db"
    monkeypatch.setattr(models, "DB_NAME", test_db)
    models.init_db()

    app_module.app.config['TESTING'] = True
    test_client = app_module.app.test_client()

    yield test_client

    if os.path.exists(test_db):
        os.remove(test_db)

def test_create_task_success(client):
    response =client.post("/tasks", json={"title": "Buy milk"})
    data = response.get_json()

    assert response.status_code == 201
    assert data["title"] == "Buy milk"
    assert data["completed"] is False
    assert data["id"] is not None

def test_create_task_missing_title(client):
    response = client.post("/tasks", json={})
    data = response.get_json()

    assert response.status_code == 400
    assert "error" in data

def test_list_tasks_empty(client):
    response = client.get("/tasks")
    data = response.get_json()

    assert response.status_code == 200
    assert data == []


def test_list_tasks_after_creating_one(client):
    client.post("/tasks", json={"title": "Walk the dog"})
    response = client.get("/tasks")
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["title"] == "Walk the dog"

