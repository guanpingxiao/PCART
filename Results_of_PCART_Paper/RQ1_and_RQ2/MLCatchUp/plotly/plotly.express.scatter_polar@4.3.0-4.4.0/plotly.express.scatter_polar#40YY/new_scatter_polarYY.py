import plotly.express as px
df = px.data.wind()
fig = px.scatter_polar(df, 'frequency', 'direction', None, None, size=None, hover_name=None, hover_data=None, range_theta=None)