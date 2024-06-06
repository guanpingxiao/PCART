import plotly.express as px
df = px.data.gapminder()
fig = px.area(df, 'year', 'pop', line_group='country', facet_col_wrap=0)