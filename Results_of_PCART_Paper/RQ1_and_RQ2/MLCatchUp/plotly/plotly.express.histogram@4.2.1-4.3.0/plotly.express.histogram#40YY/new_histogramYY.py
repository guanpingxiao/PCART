import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, facet_col=None, hover_name=None, hover_data=None, facet_col_wrap=0)