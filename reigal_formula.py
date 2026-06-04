import data_cleanup as dc
import numpy as np
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
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
    ## the linear regression function needs 
    model = LinearRegression(fit_intercept=True)

    model.fit(log_d, log_t)

    # The slope IS your personal exponent
    
    return model.coef_[0] , model


def plot_exponent_fit(runs: list, model):
    """Plot your runs and the fitted Riegel regression line."""
    distances = np.array([r.distance for r in runs])
    times = np.array([r.time for r in runs])

    d_range = np.linspace(distances.min(), distances.max(), 200)
    log_t_pred = model.predict(np.log(d_range).reshape(-1, 1))

    plt.figure(figsize=(8, 5))
    plt.scatter(distances, times, color="steelblue", label="Your runs", zorder=5)
    plt.plot(d_range, np.exp(log_t_pred), color="tomato",
             label=f"Fit (exponent = {model.coef_[0]:.4f})")
    plt.xlabel("Distance")
    plt.ylabel("Time (hours)")
    plt.title("Your Personal Riegel Fit")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    
if __name__ == "__main__":
    list_holder = dc.runs
    exponent, model = fit_personal_exponent(list_holder)
    print("Your personal Riegel exponent:", exponent)
    plot_exponent_fit(list_holder,model)
    
    