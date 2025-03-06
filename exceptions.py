class ServiceError(Exception):
    """Base exception for external service failures"""
    def __init__(self, message: str = "Service unavailable"):
        super().__init__(message)
        self.message = message

class ConfigurationError(Exception):
    """Raised for invalid configuration"""
