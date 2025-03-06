import click
from typing import Optional
from .modules.weather import WeatherService
from .modules.nlp import NLPEngine
from .logging import configure_logging
from .exceptions import ServiceError

@click.group()
@click.option("--verbose", is_flag=True, help="Enable debug logging")
def cli(verbose: bool):
    """Antara Command Line Interface"""
    configure_logging("DEBUG" if verbose else "INFO")

@cli.command()
@click.argument("query")
def ask(query: str):
    """Process natural language query"""
    try:
        nlp = NLPEngine()
        weather_service = WeatherService()
        
        intent = nlp.classify_intent(query)
        
        if intent == "weather":
            result = weather_service.get_current_weather()
            click.echo(f"Weather: {result}")
        else:
            click.echo("I can help with weather information")
            
    except ServiceError as e:
        click.echo(f"Error: {e.message}", err=True)
