import os
import csv
from datetime import date

CSV_FILE = "liftlog_data.csv"
FIELD_NAMES = ["exercise", "sets", "reps", "weight", "date"]

def ensure_file_exists(): 
    if not os.path.exists(CSV_FILE) or os.path.getsize(CSV_FILE) == 0:
        with open(CSV_FILE, mode="w", newline="") as f:
            writer=csv.DictWriter(f, fieldnames=FIELD_NAMES)
            writer.writeheader()

def save_entry(exercise, sets, reps, weight):
    ensure_file_exists()
    entry = {
            "exercise": exercise,
            "sets": sets,
            "reps": reps,
            "weight": weight,
            "date": date.today().isoformat(),
            }
    with open(CSV_FILE, mode="a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELD_NAMES)
        writer.writerow(entry)
    return entry

def get_all_entries():
    ensure_file_exists()
    with open(CSV_FILE, mode="r", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

if  __name__ == "__main__":
    print("Saving a test entry...")
    saved = save_entry("bench press", 3, 8, 185)
    print("Saved:", saved)

    print("\nSaving another...")
    saved2 = save_entry("squat", 4, 6, 225)
    print("Saved:", saved2)

    print("\nAll entries so far:")
    for entry in get_all_entries():
        print(entry)
