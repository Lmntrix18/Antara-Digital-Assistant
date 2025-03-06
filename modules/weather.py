import requests
from typing import Optional
from .exceptions import ServiceError
from ..config import settings

class WeatherService:
    """Open-meteo API client with error handling"""
    
    TIMEOUT = 10.0
    RETRIES = 3

    def get_current_weather(self, lat: Optional[float] = None, 
                          lon: Optional[float] = None) -> str:
        """Fetch weather data with retry logic"""
        params = {
            "latitude": lat or settings.DEFAULT_LATITUDE,
            "longitude": lon or settings.DEFAULT_LONGITUDE,
            "current_weather": "true"
        }

        for _ in range(self.RETRIES):
            try:
                response = requests.get(
                    settings.WEATHER_API_URL,
                    params=params,
                    timeout=self.TIMEOUT
                )
                response.raise_for_status()
                data = response.json()
                return f"{data['current_weather']['temperature']}°C"
            except (requests.RequestException, KeyError) as e:
                raise ServiceError(f"Weather service error: {str(e)}") from e
