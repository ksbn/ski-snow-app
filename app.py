import streamlit as st
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

# --- Page config ---
st.set_page_config(page_title="⛷️ Ski Snow Report", page_icon="⛷️")

st.title("⛷️ Ski Resort Snow Report")
st.markdown("Check real-time snow conditions for any ski resort in the world.")

# --- Search ---
resort = st.text_input("🔍 Enter a ski resort name", placeholder="e.g. Verbier, Zermatt, Chamonix...")

if st.button("Search ❄️") and resort:
    with st.spinner("Fetching snow conditions..."):
        location, conditions = get_resort_weather(resort)

    if not location:
        st.error("Resort not found. Try another name.")
    else:
        description = get_weather_description(conditions["weathercode"])
        snow_depth = conditions["snow_depth"] * 100

        st.success(f"🏔️ {location['name']}, {location['country']}")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("🌡️ Temperature", f"{conditions['temperature_2m']}°C")
            st.metric("❄️ Snowfall now", f"{conditions['snowfall']} cm/h")

        with col2:
            st.metric("🌨️ Snow depth", f"{snow_depth:.0f} cm")
            st.metric("💨 Wind speed", f"{conditions['windspeed_10m']} km/h")

        st.info(f"🌤️ Conditions: {description}")