from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
import storage

app = FastAPI()

class WorkoutEntry(BaseModel):
    exercise: str
    sets: int
    reps: int
    weight: float

app.add_middleware(
	CORSMiddleware,
    allow_origins=["*"],
	allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/log")
def log_workout(entry: WorkoutEntry):
	saved = storage.save_entry(entry.exercise, entry.sets, entry.reps, entry.weight)
	return saved

@app.get("/history")
def history():
	return storage.get_all_entries()

if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="0.0.0.0", port=8080)

app.mount("/", StaticFiles(directory=".", html=True), name="static	")

