import plotly.express as px
df = px.data.tips()
fig = px.violin(df, None, 'total_bill', None, None, None, None, None, None, None, None, {}, {}, None, {}, 'v', 'group', log_x=False, log_y=False, range_x=None, range_y=None, points=None, box=False, title=None, template=None, width=None, facet_col_wrap=0)