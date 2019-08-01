from dashboard_helpers import get_df_from_sql, weekly_bar_chart

import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.tools import make_subplots as subplots
import plotly.graph_objs as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(
    html.Div([
        html.H4('Customer Satisfaction Dashboard'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(id='interval-component',
                     interval=60*1000, #in milliseconds
                     n_intervals=0)
    ])
)

@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    df = get_df_from_sql()
    df_weekly = weekly_bar_chart(df)

    # Create the graph with subplots
    fig = subplots(rows=1, cols=1, vertical_spacing=0.2,
                   subplot_titles=("Previous 7 Days' Performance",))

    fig['layout']['margin'] = {
        'l': 30, 'r': 10, 'b': 30, 't': 20
    }
    fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

    fig.append_trace(go.Bar(name='Bad', x=df_weekly.index, y=df_weekly['1'], marker={'color': '#d62728'}), 1, 1)
    fig.append_trace(go.Bar(name='Fair', x=df_weekly.index, y=df_weekly['2'], marker={'color': '#ff7f0e'}), 1, 1)
    fig.append_trace(go.Bar(name='Good', x=df_weekly.index, y=df_weekly['3'], marker={'color': '#2ca02c'}), 1, 1)


    return fig


if __name__ == '__main__':
    app.run_server(debug=True, port = 8000)