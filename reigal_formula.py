import data_cleanup
import numpy as np
from sklearn.linear_model import LinearRegression

RIEGEL_DEFAULT = 1.06

def riegel_predict(known_distance, known_time_hrs, target_distance, exponent=RIEGEL_DEFAULT):
    """Predict finish time (hours) for target_distance given a known effort."""
    return known_time_hrs * (target_distance / known_distance) ** exponent
