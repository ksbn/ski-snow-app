# ⛷️ Ski Resort Snow App

A Python desktop app that shows real-time snow conditions for any ski resort in the world.

## ✨ Features

- 🔍 Search any ski resort by name
- 🌡️ Current temperature
- ❄️ Live snowfall and snow depth
- 💨 Wind speed
- 🌤️ Weather conditions description
- 🆓 No API key needed — uses free Open-Meteo API

## 🛠️ Tech Stack

- Python 3
- `tkinter` — desktop UI
- `requests` — API calls
- [Open-Meteo API](https://open-meteo.com/) — free weather data
- [Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api) — resort name → coordinates

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/ksbn/ski-snow-app.git
cd ski-snow-app

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python3 main.py
```

## 📁 Project Structure

```
ski-snow-app/
├── main.py          # UI and app logic
├── weather.py       # API calls and data fetching
├── requirements.txt # Dependencies
└── README.md
```

## 🏔️ Example Resorts to Try

- Verbier (Switzerland)
- Zermatt (Switzerland)
- Chamonix (France)
- Baqueira (Spain)
- Innsbruck (Austria)

## 🎯 What I Learned

- Fetching data from a real REST API
- Converting location names to coordinates using geocoding
- Building desktop UIs with tkinter
- Structuring a Python project with modules