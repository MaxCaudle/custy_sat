<<<<<<< HEAD
from dashboard_helpers import Data, get_locations
import datetime
>>>>>>> d60105b944916b291c29d52c6362818d7a71e195

import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.tools import make_subplots as subplots
import plotly.graph_objs as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
locations = get_locations()


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
                     interval=60*1000, #in milliseconds
                     n_intervals=0)
    ])
)

@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals'),
               Input('location_selector', 'value')])
def update_graph_live(n, location):
    data = Data(locations)
    # Create the graph with subplots
    fig = subplots(rows=1, cols=1, vertical_spacing=0.2,
                   subplot_titles=("Previous 7 Days' Performance",))

    fig['layout']['margin'] = {
        'l': 30, 'r': 10, 'b': 30, 't': 20
    }
    fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

<<<<<<< HEAD
    df_weekly = data.df_week[location]
    fig.append_trace(go.Bar(name='Bad', x=df_weekly.index, y=df_weekly['1']), 1, 1)
    fig.append_trace(go.Bar(name='Fair', x=df_weekly.index, y=df_weekly['2']), 1, 1)
    fig.append_trace(go.Bar(name='Good', x=df_weekly.index, y=df_weekly['3']), 1, 1)
======+
>>>>>>> d60105b944916b291c29d52c6362818d7a71e195

    return fig


if __name__ == '__main__':
    app.run_server(debug=True, port = 8000)