import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, 'year', 'lifeExp', None, None, None, None, None, None, None, None, None, 0, None, None, None, None, None, None, animation_frame=None, animation_group=None, category_orders=None, labels=None, orientation=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)