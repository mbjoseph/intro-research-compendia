import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

d = pd.read_csv("data/clean/data_clean.csv")

# get 2020 data
d = d[(d['date'] > '2020-01-01') & (d['date'] < '2021-01-01')]

# add a column to indicate weekends
d["dow"] = pd.to_datetime(d.date).dt.dayofweek # monday=0
d["is_weekend"] = d["dow"] >= 5

# plot accidents by date
plt.figure(figsize=(15,4))
plt.xticks(rotation=90)
plt.plot(d["date"], d["n_incidents"], c="k", alpha=0.2)
plt.scatter(d["date"], d["n_incidents"], c=d["is_weekend"], cmap="bwr")
plt.ylabel("Number of accidents")
plt.xlabel("Date")
plt.savefig(fname=Path("figures/awesome_plot.png"), dpi=300, bbox_inches="tight")
