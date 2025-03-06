
from datetime import datetime
import re
from modules.calendar import CalendarManager
from modules.email import EmailClient

from modules.entertainment import EntertainmentSystem
from modules.productivity import TaskManager
import datetime

class CommandHandler:
    def __init__(self):
        self.calendar = CalendarManager()
        self.email = EmailClient()
        
        self.entertainment = EntertainmentSystem()
        self.tasks = TaskManager()

    def process_command(self, command: str) -> str:
        command = command.lower()
        
        # Calendar Commands
        if "add event" in command:
            return self._handle_calendar(command)
            
        # Email Commands
        if "send email" in command:
            return self._handle_email(command)
            
        # Smart Home Commands
        if any(word in command for word in ["light", "thermostat"]):
            return self._handle_smart_home(command)
            
        # Productivity Commands
        if "add task" in command:
            return self._handle_tasks(command)
            
        # Entertainment Commands
        if "tell joke" in command:
            return self.entertainment.tell_joke()
            
        return "Command not recognized"

    def _handle_calendar(self, command: str) -> str:
        # NLP parsing for time/event extraction
        try:
            time_str = "10:00"  # Extract from command
            event_name = "meeting"  # Extract from command
            self.calendar.add_event(event_name, time_str)
            return f"Added {event_name} at {time_str} to your calendar"
        except ValueError:
            return "Invalid time format. Please use HH:MM"

    def _handle_email(self, command: str) -> str:
        # Extract recipient and message from command
        self.email.send_email("recipient@example.com", "Reminder", "Your meeting starts soon")
        return "Email sent successfully"

   

    def _handle_tasks(self, command: str) -> str:
        task = command.replace("add task", "").strip()
        self.tasks.add_task(task)
        return f"Added '{task}' to your todo list"
