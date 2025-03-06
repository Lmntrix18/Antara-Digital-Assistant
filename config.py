from pydantic import BaseSettings, AnyUrl

class Settings(BaseSettings):
    WEATHER_API_URL: AnyUrl = "https://api.open-meteo.com/v1/forecast"
    NEWS_RSS_FEED: AnyUrl = "http://feeds.bbci.co.uk/news/rss.xml"
    DEFAULT_LATITUDE: float = 51.5074
    DEFAULT_LONGITUDE: float = -0.1278

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
