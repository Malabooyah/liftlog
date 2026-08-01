import csv
import os
import subprocess
from datetime import date

FILE = os.path.expanduser("~/liftlog/data.csv")
REPO = os.path.expanduser("~/liftlog")

def ensure_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "exercise", "sets", "reps", "weight"])

def git_sync():
    try:
        subprocess.run(["git", "add", "data.csv"], cwd=REPO, check=True)
        subprocess.run(["git", "commit", "-m", f"log entry {date.today()}"], cwd=REPO, check=True)
        subprocess.run(["git", "push"], cwd=REPO, check=True)
        print("Synced to GitHub.")
    except subprocess.CalledProcessError:
        print("Nothing new to sync, or push failed.")

def log_entry():
    exercise = input("Exercise: ")
    sets = input("Sets: ")
    reps = input("Reps: ")
    weight = input("Weight: ")
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date.today(), exercise, sets, reps, weight])
    print("Logged.")
    git_sync()

def view_entries():
    with open(FILE) as f:
        for row in csv.reader(f):
            print(" | ".join(row))

def main():
    ensure_file()
    while True:
        print("\n1) Log workout  2) View history  3) Quit")
        choice = input("> ")
        if choice == "1":
            log_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
