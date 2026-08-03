# LiftLog

A workout tracker that started as a Python CLI tool and grew into a full-stack, installable Progressive Web App.

## Live Demo

https://liftlog-a3gu.onrender.com/ — open in Chrome on mobile and tap "Add to Home Screen" to install it as a real app. Note: free-tier hosting spins down after 15 minutes of inactivity, so the first load after idle time may take 30-60 seconds to wake up.

## Current Status

✅ CSV-backed storage layer (tested, handles create + read)
✅ FastAPI backend with `/log` (POST) and `/history` (GET) endpoints
✅ Frontend UI — form for logging sets, live history display, no page reloads
✅ Frontend and backend consolidated into a single FastAPI app (no more separate ports/CORS)
✅ PWA layer complete — manifest.json, service worker, custom app icon
✅ Deployed live on Render (Docker-based), confirmed installed and working on mobile
⏳ Automated test suite (pytest) and CI via GitHub Actions — in progress

## Architecture

CSV file <- storage.py (save_entry, get_all_entries) <- main.py (FastAPI: /log, /history, serves static files) <- index.html (form + history UI, calls API on same origin) <- manifest.json + sw.js (PWA install + offline shell caching)

Frontend and backend are served from the same FastAPI app — index.html, manifest.json, sw.js, and the icons are all served as static files by the same process that handles the /log and /history API routes. This means the frontend calls relative paths (/history, not a hardcoded URL), so there's nothing to break when moving between environments.

## Tech Stack

Backend: Python, FastAPI, uvicorn. Storage: CSV (via Python's csv module) — intentionally simple for a personal project; not tracked in git (see .gitignore). Frontend: Vanilla HTML/CSS/JS, no framework. PWA: Web App Manifest + Service Worker (cache-first for static shell, network-passthrough for API calls). Hosting: Render, free tier, Docker-based deploy.

## Running Locally

Backend: pip install -r requirements.txt, then python main.py — starts on http://localhost:8000. Frontend: since main.py now serves the frontend too, just visiting http://localhost:8000 in a browser loads the full app — no separate frontend server needed.

## What's Left

Add pytest test coverage for storage.py and main.py. Add a GitHub Actions workflow to run those tests automatically on every push and pull request. Optionally add persistent storage if this grows beyond a demo, since free-tier hosting resets the filesystem on redeploy.
