import plotly.express as px
df = px.data.tips()
fig = px.strip(df, 'total_bill', 'day', None, None, None, None, None, None, None, None, {}, {}, None, {}, orientation='v', stripmode='group', log_x=False, log_y=False, facet_col_wrap=0)