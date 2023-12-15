# my_dash_app/pages/dashboard_page.py
from dash import html, dcc, callback_context, Output, Input  # Import Output and Input
import plotly.express as px
from app import app  # Import the app variable
import os
import json
import pandas as pd

# Load data
data_folder = os.path.join(os.getcwd(), 'data')
with open(os.path.join(data_folder, 'karnataka.json'), 'r') as f:
    geojson = json.load(f)

# Check if the CSV file exists before attempting to read it
csv_file_path = os.path.join(data_folder, 'water_data5.csv')
if os.path.exists(csv_file_path):
    df = pd.read_csv(csv_file_path)
    print(df.head())  # Print the first 5 rows of the DataFrame
else:
    raise FileNotFoundError(f"CSV file not found at: {csv_file_path}")

def layout(df, geojson):
    return html.Div(style={'backgroundColor': '#f2f2f2'}, children=[
        html.H1("Groundwater Analysis", style={'textAlign': 'center', 'color': '#333333'}),
        dcc.Slider(
            id='year-slider',
            min=2015,
            max=2020,
            value=2015,
            marks={str(year): str(year) for year in range(2015, 2021)},
            step=None
        ),
        dcc.Graph(id='choropleth', clickData=None, style={'padding': '10px'}),
        html.Br(),
        dcc.Graph(id='scatter_geo', clickData=None, style={'padding': '10px'}),
        html.Br(),
        dcc.Markdown(id='click-data', children="Click on a point in the scatter plot to see more details.", style={'color': 'red'})
    ])

@app.callback(
    Output('choropleth', 'figure'),
    [Input('year-slider', 'value')]
)
def update_choropleth(selected_year):
    filtered_df = df[df['Date Collection'] == selected_year]

    print("Filtered Data for Choropleth:")
    print(filtered_df.head())

    fig = px.choropleth_mapbox(filtered_df, 
                                geojson=geojson, 
                                locations='district',  # Correct the column name
                                color='cl',
                                featureidkey="properties.district",
                                center={"lat": filtered_df['Latitude'].mean(), "lon": filtered_df['Longitude'].mean()},
                                mapbox_style="carto-positron", 
                                zoom=5,
                                hover_data=['Station Name', 'Agency Name', 'district', 'ph_gen'])
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return fig

@app.callback(
    Output('scatter_geo', 'figure'),
    [Input('year-slider', 'value')]
)
def update_scatter_geo(selected_year):
    filtered_df = df[df['Date Collection'] == selected_year]

    print("Filtered Data for Scatter Plot:")
    print(filtered_df.head())

    fig = px.scatter_geo(filtered_df, 
                         lat='latitude',  # Correct the column name
                         lon='longitude',  # Correct the column name
                         color='cl',
                         hover_data=['Station Name', 'Agency Name', 'district', 'ph_gen'])
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return fig

@app.callback(
    Output('click-data', 'children'),
    [Input('scatter_geo', 'clickData'),
     Input('year-slider', 'value')]
)
def display_click_data(clickData, selected_year):
    if clickData is None:
        return "Click on a point in the scatter plot to see more details."
    else:
        # Get the index of the clicked point
        point_index = clickData['points'][0]['pointIndex']
        # Filter the dataframe for the selected year
        filtered_df = df[df['Date Collection'] == selected_year]
        # Get the data of the clicked point
        point_data = filtered_df.iloc[point_index]
        return f"""
        Station Name: {point_data['Station Name']}
        Agency Name: {point_data['Agency Name']}
        District: {point_data['district']}
        pH_gen: {point_data['ph_gen']}
        """
