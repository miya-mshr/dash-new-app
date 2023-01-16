from dash import Dash, dcc, html, Input, Output
import os
import plotly.express as px
import dash_core_components as dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
core_style = {"width": "80%", "margin": "5% auto"}

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(['LA', 'NYC', 'MTL'],
        'LA',
        id='dropdown'
    ),
    html.Div(id='display-value')
    dcc.Graph(
        figure=px.bar(x=[1,2,3,4,5], y=[1,2,3,4,5]),
        style=core_style,
    ),
])

@app.callback(Output('display-value', 'children'),
                [Input('dropdown', 'value')])
def display_value(value):
    return f'You have selected {value}'

if __name__ == '__main__':
    app.run_server(debug=True)
