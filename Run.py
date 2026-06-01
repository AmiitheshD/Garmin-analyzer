from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Union


class Run(BaseModel):
    date: datetime
    distance: float
    moving_time: str
    avg_hr: int
    total_ascent: int
    total_descent: int
    avg_power: int
    
    
    def time_fix(self):
        """Basic parse of `moving_time` into total seconds.

        Assumes input is well-formed and numeric. Handles:
        - "SS"
        - "MM:SS"
        - "HH:MM:SS"

        Returns int(total_seconds) or `None` for unexpected part counts.
        (Exceptions from bad input are not caught here.)
        """
        t = str(self.moving_time)
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

        return hours * 3600 + minutes * 60 + seconds
    
    
    


        
       