import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# Dash-App erstellen
app = dash.Dash(__name__)
server = app.server

# Sidebar Layout
sidebar = html.Div(
    id='sidebar',
    style={
        'position': 'fixed',
        'top': 0,
        'left': 0,
        'bottom': 0,
        'width': '250px',
        'background-color': '#f8f9fa',
        'padding': '10px',
    },
    children=[
        html.H2("Navigation"),
        dcc.Link('Gesamtüberblick', href='/gesamtueberblick', style={'display': 'block', 'margin-bottom': '10px'}),
        dcc.Link('Überblick nach Jahr', href='/ueberblick_nach_jahr', style={'display': 'block', 'margin-bottom': '10px'}),
        dcc.Link('Länderanalyse', href='/laenderanalyse', style={'display': 'block', 'margin-bottom': '10px'}),
        # Weitere Links für Unterkategorien hinzufügen
    ]
)

# Content-Bereich Layout
content = html.Div(
    id='content',
    style={
        'margin-left': '250px',  # Platz für Sidebar
        'padding': '20px',
    }
)

# Gesamtüberblick Graph
def create_gesamtueberblick_graph():
    # Hier kannst du den ersten Graphen für den Gesamtüberblick hinzufügen
    df = pd.read_csv('data/1gesamt_deutschland.csv')
    fig = go.Figure()
    for col, name, color in zip(
        ['gesamt_export', 'gesamt_import', 'gesamt_handelsvolumen'],
        ['Exportvolumen', 'Importvolumen', 'Gesamthandelsvolumen'],
        ['#1f77b4', '#ff7f0e', '#2ca02c']
    ):
        fig.add_trace(go.Scatter(
            x=df['Jahr'],
            y=df[col],
            mode='lines+markers',
            name=name,
            line=dict(width=2, color=color),
            hovertemplate=f'<b>{name}</b><br>Jahr: %{{x}}<br>Wert: %{{y:,.0f}} €'
        ))
    return fig

# Layout der Dash-App
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    sidebar,  # Die Sidebar zur Navigation
    content,  # Der Content-Bereich für die Graphen
])

# Callback zur Navigation und zum Graphen-Update
@app.callback(
    Output('content', 'children'),
    Input('url', 'pathname')
)
def update_content(pathname):
    if pathname == '/gesamtueberblick':
        return dcc.Graph(figure=create_gesamtueberblick_graph())
    elif pathname == '/ueberblick_nach_jahr':
        # Hier kannst du den Graphen für die zweite Unterkategorie hinzufügen
        return html.Div("Monatlicher Handelsverlauf nach Jahr (noch nicht implementiert)")
    elif pathname == '/laenderanalyse':
        # Hier kannst du die Länderanalyse-Graphen hinzufügen
        return html.Div("Länderanalyse (noch nicht implementiert)")
    else:
        return html.Div("Wähle eine Kategorie aus der Sidebar")

if __name__ == '__main__':
    app.run_server(debug=True)
