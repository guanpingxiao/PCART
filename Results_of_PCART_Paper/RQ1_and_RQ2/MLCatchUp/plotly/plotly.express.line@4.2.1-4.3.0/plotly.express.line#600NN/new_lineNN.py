import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, 'year', 'lifeExp', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, {}, {}, None, {}, None, {}, False, False, None, None, None, 'auto', title=None, template=None, width=None, height=None, facet_col_wrap=0)