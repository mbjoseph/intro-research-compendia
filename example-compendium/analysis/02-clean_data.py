""" Summarize daily traffic data """

import pandas as pd
from pathlib import Path

data_path = Path("data/raw/data.csv")
d = pd.read_csv(data_path, low_memory=False)

# get number of accidents per day
d['occurrence_date'] = pd.to_datetime(d['FIRST_OCCURRENCE_DATE']).dt.date
daily_summaries = d.groupby('occurrence_date').count()[["INCIDENT_ID"]]
daily_summaries = daily_summaries.reset_index()
daily_summaries.rename(
    columns={"occurrence_date": "date", "INCIDENT_ID": "n_incidents"},
    inplace=True
)
daily_summaries.to_csv(Path("data/clean/data_clean.csv"))
