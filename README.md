# LiftLog

A command-line workout tracker that runs entirely on my Android phone. No app, no server, just Python and a terminal.

## Why I built this

I'm transitioning into software development after years in admin/operations roles, and I wanted a project that was actually mine — something built for a problem I have, not a tutorial exercise. I lift seriously and track my training closely, so a logging tool made sense as a first real project.

It's also become a testbed for a bigger idea: how far can you push a phone as an actual dev environment, not just a place to check email? Turns out, pretty far.

## How it works

- Python script running in Termux (a full Linux terminal environment for Android)
- Logs each set — exercise, sets, reps, weight — to a CSV file
- Triggered from a home screen widget via Termux:Widget, so logging a set is a single tap, no need to manually open a terminal
- Auto-commits and pushes the data to this repo after every entry, so training history is version-controlled and backed up without me doing anything extra

## What's next

Planning to rebuild this as a full-stack app — FastAPI backend, proper database instead of a flat CSV, and a dashboard for visualizing progression over time. This version stays as-is: a working proof that the phone-only workflow holds up end to end.
