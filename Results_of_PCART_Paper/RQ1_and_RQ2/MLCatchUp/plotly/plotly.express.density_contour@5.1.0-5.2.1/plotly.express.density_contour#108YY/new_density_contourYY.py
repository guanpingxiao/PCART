import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df, 'total_bill', 'tip', None, None, None, None, 0, None, None, hover_name=None, hover_data=None, animation_frame=None, animation_group=None, trendline_options=None, trendline_scope='trace')