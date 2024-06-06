import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, 'frequency', theta='direction', color='strength', range_theta=None)