from pydantic import BaseModel
from datetime import datetime    
class Run(BaseModel):
    date: datetime
    distance: float
    moving_time: str
    avg_hr: int
    total_ascent: int
    total_descent: int
    avg_power: int
    
    @property
    def time(self):
        """Basic parse of `moving_time` into total seconds.

        Assumes input is well-formed and numeric. Handles:
        - "SS"
        - "MM:SS"
        - "HH:MM:SS"

        Returns int(total_seconds) or `None` for unexpected part counts.
        (Exceptions from bad input are not caught here.)
        """
        t = self.moving_time
        parts = [int(p) for p in t.split(":")]

        if len(parts) == 1:
            hours = 0
            minutes = 0
            seconds = parts[0]
        elif len(parts) == 2:
            hours = 0
            minutes, seconds = parts
        elif len(parts) == 3:
            hours, minutes, seconds = parts
        else:
            return None

        return hours + (minutes / 60) + (seconds / 3600)
    
    @property
    def pace(self):
        """Return speed in miles per hour.

        Uses `self.time` (hours) and `self.distance` (assumed kilometers),
        converts distance to miles, and divides by hours.
        """
        hours = self.time
        miles = self.distance 
        if not hours:
            return None
        return miles / hours


        
       

