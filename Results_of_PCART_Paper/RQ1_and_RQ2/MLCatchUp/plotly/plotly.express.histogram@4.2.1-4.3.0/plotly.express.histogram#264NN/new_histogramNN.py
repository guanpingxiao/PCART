import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, None, None, None, None, None, {}, {}, color_discrete_sequence=None, color_discrete_map={}, marginal=None, opacity=None, orientation='v', barmode='relative', barnorm=None, histnorm=None, log_x=False, log_y=False, facet_col_wrap=0)