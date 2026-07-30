from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_home():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Welcome to LearnSync API 🚀"
    }


def test_get_resources():
    response = client.get("/resources")
    assert response.status_code == 200
    resources = response.json()
    assert isinstance(resources, list)
    assert len(resources) > 0
    first = resources[0]
    assert "id" in first
    assert "title" in first
    assert "resource_type" in first
    assert "status" in first


def test_dashboard():
    response = client.get("/analytics/dashboard")
    assert response.status_code == 200
    dashboard = response.json()
    assert "total_spaces" in dashboard
    assert "total_resources" in dashboard
    assert "completed_resources" in dashboard
    assert "in_progress_resources" in dashboard
    assert "not_started_resources" in dashboard
    assert "total_notes" in dashboard
    assert "total_tags" in dashboard
    assert "pending_revisions" in dashboard
    assert "completion_percentage" in dashboard

    assert isinstance(dashboard["total_spaces"], int)
    assert isinstance(dashboard["total_resources"], int)
    assert isinstance(dashboard["completed_resources"], int)
    assert isinstance(dashboard["in_progress_resources"], int)
    assert isinstance(dashboard["not_started_resources"], int)
    assert isinstance(dashboard["total_notes"], int)
    assert isinstance(dashboard["total_tags"], int)
    assert isinstance(dashboard["pending_revisions"], int)
    assert isinstance(dashboard["completion_percentage"], float)


def test_register():
    payload = {
        "username": "Test User",
        "email": "testuser134@gmail.com",
        "password": "test1234"
    }

    response = client.post("/auth/register", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]
    assert "id" in data
    assert "created_at" in data


def test_login():
    payload = {
        "email": "testuser123@gmail.com",
        "password": "test1234"
    }

    response = client.post("/auth/login", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"