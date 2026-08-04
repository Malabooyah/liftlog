import storage

def test_save_and_get_entry(tmp_path, monkeypatch):
    test_file = tmp_path / "test_workouts.csv"
    monkeypatch.setattr(storage, "CSV_FILE", str(test_file))

    entry = storage.save_entry("bench press", 3, 8, 185)
    assert entry["exercise"] == "bench press"

    entries = storage.get_all_entries()
    assert len(entries) == 1
    assert entries[0]["exercise"] == "bench press"
