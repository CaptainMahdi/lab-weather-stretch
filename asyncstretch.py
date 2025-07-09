import asyncio
import httpx
from rich import print

async def get_coordinates(city: str):
    geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    async with httpx.AsyncClient() as client:
        response = await client.get(geocode_url)
        data = response.json()
        if data["results"]:
            latitude = data["results"][0]["latitude"]
            longitude = data["results"][0]["longitude"]
            return latitude, longitude
        else:
            raise ValueError("City not found.")
async def get_weather(latitude: float, longitude: float):
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    async with httpx.AsyncClient() as client:
        response = await client.get(weather_url)
        data = response.json()
        temperature = data["current_weather"]["temperature"]
        windspeed = data["current_weather"]["windspeed"]
        condition_code = data["current_weather"]["weathercode"]
        return temperature, windspeed, condition_code
async def get_news(city: str):
    gnews_url = f"https://gnews.io/api/v4/search?q=example&lang=en&country=us&max=10&apikey=eff0093081e326ce9efb9e4ac7440e00"
    async with httpx.AsyncClient() as client:
        response = await client.get(gnews_url)
        data = response.json()
        if data["articles"]:
            top_article = data["articles"][0]["title"]
            return top_article
        else:
            return "No local news found."
async def get_second_news(city: str):
    gnews2_url = f"https://gnews.io/api/v4/search?q=example&lang=en&country=us&max=10&apikey=eff0093081e326ce9efb9e4ac7440e00"
    async with httpx.AsyncClient() as client:
        response = await client.get(gnews2_url)
        data = response.json()
        if data["articles"]:
            top_article = data["articles"][1]["title"]
            return top_article
        else:
            return "No local news found."
async def main():
    city = input("Enter a city name: ").title()
    try:
        latitude, longitude = await get_coordinates(city)
        weather, windspeed, condition_code = await get_weather(latitude, longitude)
        top_news = await get_news(city)
        second_news = await get_second_news(city)
        print(f"The weather in [green]{city}[/green] is [red]{weather}°C[/red] with a wind speed of [blue]{windspeed} km/h[/blue] and the condition code is [yellow]{condition_code}[/yellow]. The 2 top stories today are [blue]{top_news}[/blue] and [blue]{second_news}[/blue]. [orange]Happy Travels![/orange]")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    asyncio.run(main())