import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("mobile-data.csv")

fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Mobile brand"])

fig.show()