import plotly.express as px
df = px.data.tips()
fig = px.treemap(df, None, 'total_bill', None, None, None, None, None, None, None, {}, hover_name=None, path=None)