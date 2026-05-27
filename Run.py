from pydantic import BaseModel
from datetime import datetime
# class Run:
    
#     def __init__(self, date, distance, time, avg_hr, avg_pace, total_ascent, total_descent, avg_power):
#         self.date = date
#         self.distance = distance
#         self.time = time
#         self.avg_hr = avg_hr
#         self.avg_pace = avg_pace
#         self.total_ascent = total_ascent
#         self.total_descent = total_descent
#         self.avg_power = avg_power
#     def __repr__(self):
#         return (
#             f"Run(date={self.date}, distance={self.distance}, time={self.time}, "
#             f"avg_hr={self.avg_hr}, avg_pace={self.avg_pace})"
#         )
        
        
class Run(BaseModel):
    date: datetime
    distance: float
    moving_time: str
    avg_hr: int
    avg_pace: str
    total_ascent: int
    total_descent: int
    avg_power: int
    
    
test = Run(
    date=datetime(2020, 12, 4, 13, 24, 33),
    distance=4.4,
    moving_time="4:25",
    avg_hr=123,
    avg_pace="9:22",
    total_ascent=400,
    total_descent=200,
    avg_power=20
)
print(test)
           

        
