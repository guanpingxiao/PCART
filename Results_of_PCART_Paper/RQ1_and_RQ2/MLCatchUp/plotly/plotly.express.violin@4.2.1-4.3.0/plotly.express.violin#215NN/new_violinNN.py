import plotly.express as px
df = px.data.tips()
fig = px.violin(df, None, 'total_bill', None, None, None, None, None, None, None, None, {}, {}, None, {}, 'v', violinmode='group', log_x=False, log_y=False, range_x=None, facet_col_wrap=0)