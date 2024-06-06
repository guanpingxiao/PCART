import plotly.express as px
df = px.data.gapminder().query('year == 2007')
fig = px.line_geo(df, lat=None, lon=None, locations='iso_alpha', symbol=None, symbol_sequence=None, symbol_map=None, markers=False)