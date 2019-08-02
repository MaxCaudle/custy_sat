from dashboard_helpers import calc_color
import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.tools import make_subplots as subplots
import plotly.graph_objs as go
from dash.dependencies import Input, Output

def past_7_days(data, location, fig):
    df_weekly = data.df_week[location]
    ones = go.Bar(name='Bad', x=df_weekly.index, y=df_weekly['1'],
                            marker={'color': calc_color(1)})

    average = go.Scatter(x=df_weekly.index.values.tolist(),
                         y=df_weekly['mean'].values.tolist(),
                         yaxis='y3')


    twos = go.Bar(name='Fair', x=df_weekly.index, y=df_weekly['2'],
                            marker={'color': calc_color(2)})

    threes = go.Bar(name='Good', x=df_weekly.index, y=df_weekly['3'],
                            marker={'color': calc_color(3)})

    fig.append_trace(ones, 1, 1)
    fig.append_trace(twos, 1, 1)
    fig.append_trace(threes, 1, 1)
    fig.append_trace(average, 1, 1)
    print(fig.layout)
    #fig.layout.update(y3 = {'range':[0,3]})
    return fig