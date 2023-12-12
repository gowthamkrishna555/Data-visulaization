# my_dash_app/pages/front_page.py
from dash import html, dcc, dash_table
from dash.dependencies import Input, Output
from dash import callback_context

def layout():
    return html.Div(style={'backgroundColor': '#f8f9fa', 'height': '100vh'}, children=[
        html.Div(style={'textAlign': 'center', 'padding-top': '150px'}, children=[
            html.H1("Groundwater Analysis", style={'color': '#007BFF'}),
            html.H3("Explore and analyze groundwater data in Karnataka", style={'color': '#6C757D'}),
            dcc.Link(html.Button('Get Started', style={'background-color': '#007BFF', 'color': '#ffffff'}),
                     href='/dashboard')
        ]),
        html.Div([
            html.H2("Overview", style={'color': '#333333', 'margin-top': '30px'}),
            html.P("Welcome to the Groundwater Analysis app! This app allows you to explore and analyze groundwater data in Karnataka. "
                   "Navigate to the dashboard to view detailed visualizations and insights."),
            html.H2("Key Features", style={'color': '#333333', 'margin-top': '30px'}),
            html.Ul([
                html.Li("Interactive choropleth map with color-coded data"),
                html.Li("Scatter plot for geographical analysis"),
                html.Li("Detailed information on clicked points"),
                html.Li("Filter data by year and color variable")
            ]),
            html.H2("How to Use", style={'color': '#333333', 'margin-top': '30px'}),
            html.P("1. Click 'Get Started' to explore the dashboard."),
            html.P("2. Use the dropdown to select the color variable."),
            html.P("3. Adjust the slider to filter data by year."),
            html.P("4. Explore the choropleth map and scatter plot."),
            html.P("5. Click on points in the scatter plot for detailed information."),
        ], style={'max-width': '800px', 'margin': 'auto'}),
    ])
