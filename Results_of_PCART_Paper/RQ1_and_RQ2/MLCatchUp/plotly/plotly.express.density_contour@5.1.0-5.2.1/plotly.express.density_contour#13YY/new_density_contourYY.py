import plotly.express as px
df = px.data.tips()
fig = px.density_contour(data_frame=df, x='total_bill', y='tip', z=None, trendline_options=None, trendline_scope='trace')