import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df, 'total_bill', y='tip', facet_col_wrap=0)
