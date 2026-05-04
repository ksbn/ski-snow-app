import tkinter as tk
from tkinter import messagebox
from weather import get_resort_weather

WEATHER_CODES = {
    0: "Clear sky ☀️",
    1: "Mainly clear 🌤️",
    2: "Partly cloudy ⛅",
    3: "Overcast ☁️",
    71: "Slight snowfall ❄️",
    73: "Moderate snowfall ❄️❄️",
    75: "Heavy snowfall ❄️❄️❄️",
    77: "Snow grains 🌨️",
    85: "Slight snow showers 🌨️",
    86: "Heavy snow showers ❄️🌨️",
}

def get_weather_description(code: int) -> str:
    return WEATHER_CODES.get(code, "Unknown conditions")

def search():
    resort = entry.get().strip()
    if not resort:
        messagebox.showwarning("Input needed", "Please enter a ski resort name.")
        return

    result_label.config(text="Searching...")
    root.update()

    location, conditions = get_resort_weather(resort)

    if not location:
        result_label.config(text="Resort not found. Try another name.")
        return

    description = get_weather_description(conditions["weathercode"])
    snow_depth = conditions["snow_depth"] * 100  # convert to cm

    text = f"""
🏔️  {location['name']}, {location['country']}

🌡️  Temperature:  {conditions['temperature_2m']}°C
❄️  Snowfall now: {conditions['snowfall']} cm/h
🌨️  Snow depth:   {snow_depth:.0f} cm
💨  Wind speed:   {conditions['windspeed_10m']} km/h
🌤️  Conditions:   {description}
"""

    result_label.config(text=text)

# --- UI ---
root = tk.Tk()
root.title("⛷️ Ski Resort Snow App")
root.geometry("420x380")
root.resizable(False, False)
root.configure(bg="#1a1a2e")

tk.Label(root, text="⛷️ Ski Snow Report", font=("Arial", 18, "bold"),
         bg="#1a1a2e", fg="white").pack(pady=20)

entry = tk.Entry(root, font=("Arial", 14), width=24, bd=0,
                 relief="flat", bg="#16213e", fg="white",
                 insertbackground="white")
entry.pack(pady=8, ipady=8, padx=20)
entry.insert(0, "e.g. Verbier, Zermatt...")

def clear_placeholder(e):
    if entry.get() == "e.g. Verbier, Zermatt...":
        entry.delete(0, tk.END)

entry.bind("<FocusIn>", clear_placeholder)

tk.Button(root, text="Search ❄️", font=("Arial", 13, "bold"),
          bg="#6c63ff", fg="white", bd=0, padx=20, pady=8,
          cursor="hand2", command=search).pack(pady=12)

result_label = tk.Label(root, text="", font=("Arial", 13),
                        bg="#1a1a2e", fg="white",
                        justify="left", wraplength=380)
result_label.pack(padx=20)

root.mainloop()