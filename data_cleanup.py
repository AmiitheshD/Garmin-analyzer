import pandas as pd
import Run
data_frame = pd.read_csv("garmin_data.csv")
data_frame.columns = data_frame.columns.str.strip()
cols_to_keep = [
    "Date",
    "Distance",
    "Moving Time",          # or swap for Moving Time
    "Avg HR",
    "Total Ascent",
    "Total Descent",
    "Avg Power" # optional, drop if not using
]

to_drop = [i for i in data_frame.columns if i not in cols_to_keep]


data_frame.drop(columns=to_drop, inplace=True)


data_frame = data_frame.rename(columns={
    "Avg HR": "avg_hr",
    "Total Ascent": "total_ascent",
    "Total Descent": "total_descent",
    "Avg Power": "avg_power",
    "Distance": "distance",
    "Date": "date",
    "Moving Time" : "moving_time"
    
})

runs = []
for _, row in data_frame.iterrows():
    runs.append(Run.Run(
        date=row["date"],
        distance=row["distance"],
        moving_time=row["moving_time"],
        avg_hr=row["avg_hr"],
        total_ascent=row["total_ascent"],
        total_descent=row["total_descent"],
        avg_power=row["avg_power"],
    ))
    
    print(runs)




