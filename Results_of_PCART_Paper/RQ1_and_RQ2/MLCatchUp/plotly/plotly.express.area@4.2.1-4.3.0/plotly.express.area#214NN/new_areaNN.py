import plotly.express as px
df = px.data.gapminder()
fig = px.area(df, 'year', 'pop', 'country', 'continent', None, None, None, None, None, None, None, None, {}, {}, None, {}, orientation='v', groupnorm=None, log_x=False, facet_col_wrap=0)
