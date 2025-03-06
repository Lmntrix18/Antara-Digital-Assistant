
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
        self.patterns = {
            "event": r"add event (.*?) at (\d{1,2}:\d{2})",
            "email": r"send email to (\S+@\S+) about (.+)",
            "task": r"add task (.+)"
        }

    def process_command(self, command: str) -> str:
        command = command.lower()
        
        # Calendar Commands
        if "add event" in command:
            return self._handle_calendar(command)
            
        # Email Commands
        if "send email" in command:
            return self._handle_email(command)
            
        # Productivity Commands
        if "add task" in command:
            return self._handle_tasks(command)
            
        # Entertainment Commands
        if "tell joke" in command:
            return self.entertainment.tell_joke()
        if "help" in command:
            return ("I can: "
                "1. Add calendar events ('Add meeting at 18:30') "
                "2. Send emails ('Send email to janedoe@example.com about the project') "
                "3. Manage tasks ('Add task finish report') "
                "4. Tell jokes")
            
        return "Command not recognized"

    def _handle_calendar(self, command: str) -> str:
    """Extract event details from voice command"""
        try:
        # Regex to find time and event name
            time_match = re.search(r"at (\d{1,2}:\d{2})", command)
            event_match = re.search(r"add event (.*?) at", command)
        
            if not time_match or not event_match:
                return "Please specify event and time like: 'Add meeting at 18:30'"
            
            time_str = time_match.group(1)
            event_name = event_match.group(1).strip()
        
        # Validate time format
            datetime.strptime(time_str, "%H:%M")
            self.calendar.add_event(event_name, time_str)
            return f"Added '{event_name}' at {time_str} to your calendar"
        
        except ValueError:
            return "Invalid time format. Use HH:MM like 18:30"

    def _handle_email(self, command: str) -> str:
    """Parse email details from voice command"""
        try:
        # Extract recipient and message
            recipient = re.search(r"to (\S+@\S+)", command).group(1)
            message = re.search(r"about (.+)", command).group(1)
        
            if not recipient or not message:
                return "Please specify recipient and message"
            
            self.email.send_email(recipient, "Voice Command Email", message)
            return f"Email to {recipient} sent: '{message}'"
        
        except Exception as e:
            return f"Email failed: {str(e)}"
   

    def _handle_tasks(self, command: str) -> str:
        task = command.replace("add task", "").strip()
        self.tasks.add_task(task)
        return f"Added '{task}' to your todo list"
