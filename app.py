# my_dash_app/app.py
import dash
import json
import pandas as pd
from dash import dcc, html
from dash.dependencies import Input, Output
from pages import front_page, dashboard_page
import os

# Load data
data_folder = os.path.join(os.getcwd(), 'data')
with open(os.path.join(data_folder, 'karnataka.json'), 'r') as f:
    geojson = json.load(f)

df = pd.read_csv(os.path.join(data_folder, 'water_data5.csv'))

app = dash.Dash(__name__, assets_folder=os.path.join(os.getcwd(), 'assets'))

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=front_page.layout())  # Initialize with the front page
])

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/dashboard':
        return dashboard_page.layout(df, geojson)
    else:
        return front_page.layout()

if __name__ == '__main__':
    app.run_server(debug=True)
