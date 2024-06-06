import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, 'year', 'lifeExp', None, None, None, None, None, None, text=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)