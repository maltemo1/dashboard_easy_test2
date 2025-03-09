import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go

# Dash-App erstellen
app = dash.Dash(__name__)
server = app.server

# Funktion zum Erstellen eines aufklappbaren Menüs

def create_sidebar():
    return html.Div(
        id='sidebar',
        style={
            'position': 'fixed',
            'top': 0,
            'left': 0,
            'bottom': 0,
            'width': '300px',
            'background-color': '#f8f9fa',
            'padding': '10px',
            'overflow-y': 'auto'
        },
        children=[
            html.H2("Navigation"),
            dcc.Link('1. Überblick über Deutschlands Handel', href='/ueberblick_deutschland', className='main-category'),
            html.Div([
                dcc.Link('1.1 Gesamtüberblick seit 2008 bis 2024', href='/gesamtueberblick', className='sub-category'),
                dcc.Link('1.2 Überblick nach bestimmtem Jahr', href='/ueberblick_nach_jahr', className='sub-category'),
            ], className='nested-menu'),
            
            dcc.Link('2. Länderanalyse', href='/laenderanalyse', className='main-category'),
            html.Div([
                dcc.Link('2.1 Gesamtüberblick seit 2008 bis 2024', href='/laender_gesamtueberblick', className='sub-category'),
                dcc.Link('2.2 Überblick nach bestimmtem Jahr', href='/laender_nach_jahr', className='sub-category'),
                html.Div([
                    dcc.Link('Handelsbilanz & Ranking', href='/handelsbilanz_ranking', className='sub-sub-category'),
                    dcc.Link('Monatlicher Verlauf', href='/monatlicher_verlauf', className='sub-sub-category'),
                    dcc.Link('Top 10 Waren', href='/top10_waren', className='sub-sub-category'),
                ], className='nested-sub-menu'),
                dcc.Link('2.3 Überblick nach bestimmter Ware', href='/laender_nach_ware', className='sub-category'),
            ], className='nested-menu'),
            
            dcc.Link('3. Warenanalyse', href='/warenanalyse', className='main-category'),
            html.Div([
                dcc.Link('3.1 Gesamtüberblick seit 2008 bis 2024', href='/waren_gesamtueberblick', className='sub-category'),
                dcc.Link('3.2 Überblick mit mehreren Waren über bestimmten Zeitraum', href='/waren_mehrere', className='sub-category'),
            ], className='nested-menu')
        ]
    )

# Content-Bereich Layout
content = html.Div(id='content', style={'margin-left': '320px', 'padding': '20px'})

# Graph-Erstellung

def create_gesamtueberblick_graph():
    df = pd.read_csv('data/1gesamt_deutschland.csv')
    fig = go.Figure()
    for col, name, color in zip(['gesamt_export', 'gesamt_import', 'gesamt_handelsvolumen'],
                                 ['Exportvolumen', 'Importvolumen', 'Gesamthandelsvolumen'],
                                 ['#1f77b4', '#ff7f0e', '#2ca02c']):
        fig.add_trace(go.Scatter(x=df['Jahr'], y=df[col], mode='lines+markers', name=name, line=dict(width=2, color=color)))
    return fig

# Layout der Dash-App
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    create_sidebar(),
    content
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
        return html.Div("Monatlicher Handelsverlauf nach Jahr (noch nicht implementiert)")
    elif pathname == '/laenderanalyse':
        return html.Div("Länderanalyse (noch nicht implementiert)")
    else:
        return html.Div("Wähle eine Kategorie aus der Sidebar")

if __name__ == '__main__':
    app.run_server(debug=True)
