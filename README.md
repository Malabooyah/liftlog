# LiftLog

A workout tracker that started as a Python CLI tool and grew into a full-stack Progressive Web App.

## Current Status

✅ CSV-backed storage layer (tested, handles create + read)
✅ FastAPI backend with `/log` (POST) and `/history` (GET) endpoints
✅ Frontend UI — form for logging sets, live history display, no page reloads
✅ Frontend and backend consolidated into a single FastAPI app (no more separate ports/CORS)
✅ PWA layer complete — manifest.json, service worker, custom app icon
✅ Deployment prep done — Dockerfile + requirements.txt ready for Fly.io
⏳ Not yet deployed — needs real HTTPS hosting to actually install on a phone home screen (service workers require a secure context; a LAN IP doesn't qualify). Deployment is code-complete and just needs a hosting decision (Fly.io requires a payment method as of 2024; alternatives like Render are free but have cold starts).

## Architecture

--CSV file
--storage.py (save_entry, get_all_entries)
--main.py (FastAPI: /log, /history, serves static files)
--index.html (form + history UI, calls API on same origin)
--manifest.json + sw.js (PWA install + offline shell caching)

Frontend and backend are served from the same FastAPI app — index.html, manifest.json, sw.js, and the icons are all served as static files by the same process that handles the /log and /history API routes. This means the frontend calls relative paths (/history, not a hardcoded URL), so there's nothing to break when moving between environments.

## Tech Stack

Backend: Python, FastAPI, uvicorn. Storage: CSV (via Python's csv module) — intentionally simple for a personal project; not tracked in git (see .gitignore). Frontend: Vanilla HTML/CSS/JS, no framework. PWA: Web App Manifest + Service Worker (cache-first for static shell, network-passthrough for API calls). Planned hosting: Fly.io (Dockerfile-based deploy, config ready).

## Running Locally

Backend: pip install -r requirements.txt, then python main.py — starts on http://localhost:8000. Frontend: since main.py now serves the frontend too, just visiting http://localhost:8000 in a browser loads the full app — no separate frontend server needed.

## What's Left

Pick a hosting option (Fly.io paid, or a free alternative) and run fly deploy. Once live on HTTPS, confirm install-to-homescreen works on mobile. Optionally add a persistent volume if deploying to Fly, since its filesystem resets on redeploy otherwise.
