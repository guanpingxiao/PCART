import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, None, None, None, None, None, {}, {}, None, {}, None, None, 'v', 'relative', None, None, False, log_y=False, range_x=None, range_y=None, histfunc=None, cumulative=None, nbins=None, facet_col_wrap=0)