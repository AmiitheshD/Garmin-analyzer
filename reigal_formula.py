import data_cleanup as dc
import numpy as np
from sklearn.linear_model import LinearRegression

RIEGEL_DEFAULT = 1.06
##This is the basic regial formula format
def riegel_predict(known_distance, known_time_hrs, target_distance, exponent=RIEGEL_DEFAULT):
    """Predict finish time (hours) for target_distance given a known effort."""
    return known_time_hrs * (target_distance / known_distance) ** exponent


def fit_personal_exponent(runs: list) -> float:
    """
    Fit your personal Riegel exponent from a list of Run objects.
    Uses pairs of runs at different distances via log-linear regression.
    """
    # Use all unique pairs — more data = better fit
    distances = np.array([r.distance for r in runs])
    times = np.array([r.time for r in runs])  # hours
    
    log_d = np.log(distances).reshape(-1, 1)
    log_t = np.log(times)

    model = LinearRegression(fit_intercept=True)

    model.fit(log_d, log_t)

    # The slope IS your personal exponent
    return model.coef_[0]


temporary = dc.runs
print(fit_personal_exponent(temporary))