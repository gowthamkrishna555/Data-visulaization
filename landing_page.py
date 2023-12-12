# my_dash_app/pages/landing_page.py
from dash import html, dcc

def layout():
    return html.Div(style={'backgroundColor': '#f8f9fa', 'height': '100vh'}, children=[
        html.Div(style={'textAlign': 'center', 'padding-top': '150px'}, children=[
            html.H1("Groundwater Analysis", style={'color': '#007BFF'}),
            html.H3("Explore and analyze groundwater data in Karnataka", style={'color': '#6C757D'}),
            dcc.Link(html.Button('Get Started', style={'background-color': '#007BFF', 'color': '#ffffff'}),
                     href='/dashboard')
        ])
    ])
