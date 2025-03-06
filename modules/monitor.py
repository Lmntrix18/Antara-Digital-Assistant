
import psutil

class SystemMonitor:
    @staticmethod
    def get_stats() -> dict:
        return {
            "cpu": psutil.cpu_percent(),
            "memory": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage("/").percent
        }
