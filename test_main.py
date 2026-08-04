
from fastapi.testclient import TestClient
import main

client = TestClient(main.app)

def test_log_and_history(tmp_path, monkeypatch):
    test_file = tmp_path / "test_workouts.csv"
    monkeypatch.setattr(main.storage, "CSV_FILE", str(test_file))

    response = client.post("/log", json={"exercise": "squat", "sets": 4, "reps": 6, "weight": 225})
    assert response.status_code == 200

    response = client.get("/history")
    assert response.status_code == 200
    assert len(response.json()) == 1
