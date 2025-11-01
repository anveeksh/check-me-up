# PhishGuard — Check Me Up
A simple AI-assisted phishing URL & email detector (local demo).

## What this package contains
- `app.py` — Flask web app (runs on localhost)
- `model.pkl` — Trained demo ML model (RandomForest) for URL phishing prediction
- `feature_extractor.py` — feature extraction utilities
- `requirements.txt` — Python dependencies
- `templates/index.html` — Web UI
- `static/style.css` — Basic UI styling
- `train_model.py` — Script used to train the included demo model
- `README.md` — This file

## Quick start (Linux / macOS / WSL)
1. Create a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open your browser and visit `http://127.0.0.1:5000`

## Notes
- This demo model is trained on synthetic features for demonstration and learning purposes. It is **not** production-grade.
- Domain age / WHOIS checks are **disabled** in this offline demo (no internet). You can enable them later by adding a WHOIS lookup and updating the feature extractor.
- Feel free to explore the code, retrain `train_model.py` with real datasets (PhishTank / Kaggle), and improve the UI.

Project name: **Check Me Up** (PhishGuard demo)
