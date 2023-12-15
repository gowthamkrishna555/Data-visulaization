# my_dash_app/app.py
import dash
from dash import html
from dash.dependencies import Input, Output
from dash import dcc
from pages import landing_page, dashboard_page
import os
import json
import pandas as pd

# Load data
data_folder = os.path.join(os.getcwd(), 'data')
with open(os.path.join(data_folder, 'karnataka.json'), 'r') as f:
    geojson = json.load(f)

df = pd.read_csv(os.path.join(data_folder, 'water_data5.csv'))
print(df.head())  # Print the first 5 rows of the DataFrame

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/dashboard':
        return dashboard_page.layout(df, geojson)
    else:
        return landing_page.layout()

if __name__ == '__main__':
    app.run_server(debug=True)
