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
                            marker={'color': calc_color(1)},
                  yaxis='y')

    average = go.Scatter(x=df_weekly.index.values.tolist(),
                         y=df_weekly['mean'].values.tolist(),
                         yaxis='y1')


    twos = go.Bar(name='Fair', x=df_weekly.index, y=df_weekly['2'],
                            marker={'color': calc_color(2)},
                  yaxis='y')

    threes = go.Bar(name='Good', x=df_weekly.index, y=df_weekly['3'],
                            marker={'color': calc_color(3)},
                  yaxis='y')

    fig.append_trace(ones, 1, 1)
    fig.append_trace(twos, 1, 1)
    fig.append_trace(threes, 1, 1)
    fig.append_trace(average, 1, 1)

    fig['data'][-1].update(yaxis='y2')
    fig.layout.update(yaxis2 = {'range':[0,3],
                                'side': 'right',
                                'overlaying': 'y',
                                'anchor': 'x'})
    #print(fig.layout)
    return fig