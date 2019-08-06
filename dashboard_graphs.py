from dashboard_helpers import calc_color

import plotly.graph_objs as go


def past_7_days(data, location, fig):
    df_weekly = data.week_dict[location]
    ones = go.Bar(name='Bad',
                  x=df_weekly.index,
                  y=df_weekly['1'],
                  marker={'color': calc_color(1)},
                  yaxis='y')

    twos = go.Bar(name='Fair',
                  x=df_weekly.index,
                  y=df_weekly['2'],
                  marker={'color': calc_color(2)},
                  yaxis='y')

    threes = go.Bar(name='Good',
                    x=df_weekly.index,
                    y=df_weekly['3'],
                    marker={'color': calc_color(3)},
                    yaxis='y')

    average = go.Scatter(name='Day\'s Average',
                         x=df_weekly.index.values.tolist(),
                         y=df_weekly['mean'].values.tolist(),
                         yaxis='y1')

    fig.append_trace(ones, 1, 1)
    fig.append_trace(twos, 1, 1)
    fig.append_trace(threes, 1, 1)
    fig.append_trace(average, 1, 1)

    fig['data'][-1].update(yaxis='y2')
    fig.layout.update(yaxis2={'range': [0, 3],
                              'side': 'right',
                              'overlaying': 'y',
                              'anchor': 'x',
                              'showgrid':False})
    return fig


def piechart(data, location, fig):
    pie = go.Pie(labels=[1, 2, 3],
                 values=data.days_dict[location],
                 marker={'colors': [calc_color(1), calc_color(2), calc_color(3)]},
                 textinfo='label',
                 domain={'x': [0.0, 0.33], 'y': [0.0, 0.33]})
    fig.append_trace(pie, 1, 2)
    return fig
