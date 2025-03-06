from datetime import datetime, timedelta
import json
import os

class CalendarManager:
    def __init__(self):
        self.cal_file = "data/calendar.json"
        self._init_calendar()

    def _init_calendar(self):
        if not os.path.exists(self.cal_file):
            with open(self.cal_file, "w") as f:
                json.dump({"events": []}, f)

    def add_event(self, title: str, time: str, duration: int=60):
        """Add event to calendar (time format: HH:MM)"""
        new_event = {
            "title": title,
            "time": datetime.strptime(time, "%H:%M").time().isoformat(),
            "duration": duration,
            "date": datetime.now().date().isoformat()
        }
        with open(self.cal_file, "r+") as f:
            data = json.load(f)
            data["events"].append(new_event)
            f.seek(0)
            json.dump(data, f)

    def get_today_schedule(self):
        """Return today's events in natural language"""
        with open(self.cal_file, "r") as f:
            events = json.load(f)["events"]
            return [f"{e['title']} at {e['time'][:5]}" for e in events]
