import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv(
    "https://raw.githubusercontent.com/opendataby/stopcovid-19/master/stopcovid_data.csv"
)
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.date_pub, y=df.died, mode="lines+markers", name="died"))
fig.add_trace(
    go.Scatter(x=df.date_pub, y=df.recovered, mode="lines+markers", name="recovered")
)
fig.add_trace(
    go.Scatter(x=df.date_pub, y=df.infected, mode="lines+markers", name="infected")
)
fig.add_trace(
    go.Scatter(x=df.date_pub, y=df.tested, mode="lines+markers", name="tested")
)

fig.show()
