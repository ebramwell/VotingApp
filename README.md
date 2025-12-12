# Voting App (PyQt6)

A simple voting application built with PyQt6 that manages votes and displays results.

## Files

- `main.py` — Entry point for the application.
- `votes.py` — Vote management and CSV handling.
- `results.py` — Results display and calculations.
- `views/` — PyQt6 GUI views and windows.
- `models/` — Data models.
- `votes.csv` — Vote data.
- `voters.csv` — Voter registry.
- `requirements.txt` — Python dependencies.

## Setup

```powershell
python -m pip install -r requirements.txt
python main.py
```

## Notes

- The app prevents double voting using the voter registry.
- All vote and voter data is stored in CSV files.

AI-assisted work disclosure:
- Portions of the code were generated with the assistance of an AI (GitHub Copilot / GPT) and were reviewed and edited by the developer.
