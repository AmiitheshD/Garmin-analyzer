import pandas as pd
import Run
##Turns the csv file into a data frame
data_frame = pd.read_csv("garmin_data.csv")
data_frame.columns = data_frame.columns.str.strip()

##These are the only potential data coloumns we would need for the sake of the two computer models
cols_to_keep = [
    "Date",
    "Distance",
    "Moving Time",          # or swap for Moving Time
    "Avg HR",
    "Total Ascent",
    "Total Descent",
    "Avg Power",# optional, drop if not using
    "Max HR"
]
#Filtering out the data frame
to_drop = [i for i in data_frame.columns if i not in cols_to_keep]


data_frame.drop(columns=to_drop, inplace=True)

#renaming the coloumns to be more compatable with the RUN classs
data_frame = data_frame.rename(columns={
    "Avg HR": "avg_hr",
    "Total Ascent": "total_ascent",
    "Total Descent": "total_descent",
    "Avg Power": "avg_power",
    "Distance": "distance",
    "Date": "date",
    "Moving Time" : "moving_time",
    "Max HR": "max_hr"
    
})

#Turning the data frame into a list of Run classes
runs = []
for _, row in data_frame.iterrows(): #that dash means I dont care about the value
    runs.append(Run.Run(
        date=row["date"],
        distance=row["distance"],
        moving_time=row["moving_time"],
        avg_hr=row["avg_hr"],
        total_ascent=row["total_ascent"],
        total_descent=row["total_descent"],
        avg_power=row["avg_power"],
        max_hr = row["max_hr"]
    ))
    




