import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, None, None, None, None, None, {}, labels={}, color_discrete_sequence=None, color_discrete_map={}, marginal=None, facet_col_wrap=0)