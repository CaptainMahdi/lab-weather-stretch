import streamlit as st
import httpx
print(httpx.get("https://httpbin.org/get").status_code)


# Get coordinates from city name
def get_coordinates(city_name):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}"
    response = httpx.get(url)
    if response.status_code == 200:
        data = response.json()
        results = data.get("results")
        if results:
            lat = results[0]["latitude"]
            lon = results[0]["longitude"]
            return lat, lon
    return None, None

# Get weather from lat/lon
def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = httpx.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("current_weather", {})
    return {}

# Streamlit UI
st.title("🌤️ Simple Weather App")

city_name = st.text_input("Enter a city name:")

if city_name:
    lat, lon = get_coordinates(city_name)
    if lat is not None:
        weather = get_weather(lat, lon)
        if weather:
            st.subheader(f"Weather in {city_name.title()}")
            st.write(f"🌡️ Temperature: {weather.get('temperature')}°C")
            st.write(f"💨 Windspeed: {weather.get('windspeed')} km/h")
            st.write(f"🧭 Wind Direction: {weather.get('winddirection')}°")
            st.write(f"📍 Coordinates: ({lat:.2f}, {lon:.2f})")
        else:
            st.error("Weather info not available.")
    else:
        st.error("City not found. Try again.")
