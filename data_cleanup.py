import pandas as pd

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

data_frame.info()

data_frame = data_frame.rename(columns={
    "Avg HR": "avg_hr",
    "Avg Pace": "avg_pace",
    "Total Ascent": "total_ascent",
    "Total Descent": "total_descent",
    "Avg Power": "avg_power",
    "Distance": "distance",
    "Date": "date"
    
})




