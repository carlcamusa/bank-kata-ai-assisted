from abc import ABC, abstractmethod
import datetime

class Clock(ABC):
    @abstractmethod
    def today_as_string(self) -> str:
        """Returns the current date as a string in DD/MM/YYYY format."""
        pass

class SystemClock(Clock):
    def today_as_string(self) -> str:
        """Returns the system's current date as a string in DD/MM/YYYY format."""
        return datetime.datetime.now().strftime("%d/%m/%Y") 