import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, x='total_bill', y=None, color=None, pattern_shape=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, hover_name=None, hover_data=None, animation_frame=None, animation_group=None, text_auto=False)