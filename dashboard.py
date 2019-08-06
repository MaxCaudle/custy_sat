from Data import Data
from dashboard_helpers import get_locations
from dashboard_graphs import past_7_days
import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.tools import make_subplots as subplots
import plotly.graph_objs as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
locations = get_locations()
data = Data(locations)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(
    html.Div([
        html.H4('Customer Satisfaction Dashboard'),
        dcc.Dropdown(id='location_selector',
                     options=[{'label': location, 'value': location} for location in locations]
                             + [{'label':'All Locations', 'value':'all'}],
                     value='all'
                     ),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(id='interval-component',
                     interval=60*1000,  # in milliseconds
                     n_intervals=0)
    ])
)


@app.callback(Output('live-update-graph', 'figure'),
              [Input('location_selector', 'value')])
def update_graph_live(location):
    # Create the graph with subplots
    fig = subplots(rows=1, cols=2, vertical_spacing=0.2,
                   subplot_titles=("Previous 7 Days' Performance",))

    fig['layout']['margin'] = {
        'l': 40, 'r': 50, 'b': 30, 't': 20
    }
    fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

    fig = past_7_days(data, location, fig)

    return fig


@app.callback(Output('interval-component', 'interval'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    global data
    data.get_df_from_sql()
    data.make_all_weeklys()
    data.test = "set"
    return 60*1000


if __name__ == '__main__':
    app.run_server(debug=True, port=8000)
