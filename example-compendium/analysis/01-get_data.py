""" Download Denver traffic accident data """

import pandas as pd
from pathlib import Path

# https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-traffic-accidents
data_url = "https://www.denvergov.org/media/gis/DataCatalog/traffic_accidents/csv/traffic_accidents.csv"
data_path = Path("data/raw/data.csv")
d = pd.read_csv(data_url, low_memory=False)
d.to_csv(data_path)
