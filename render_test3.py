import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Kategorien und Subkategorien mit Links für zukünftige Navigation
def create_nav_structure():
    return {
        "Überblick über Deutschlands Handel": {
            "Gesamtüberblick seit 2008 bis 2024": "#",
            "Überblick nach bestimmtem Jahr": "#",
        },
        "Länderanalyse": {
            "Gesamtüberblick seit 2008 bis 2024": "#",
            "Überblick nach bestimmtem Jahr": "#",
            "Überblick nach bestimmter Ware": "#",
        },
        "Warenanalyse": {
            "Gesamtüberblick seit 2008 bis 2024": "#",
            "Überblick nach bestimmtem Jahr": "#",
            "Überblick nach bestimmtem Land": "#",
        }
    }

# Funktion zum Rendern der Sidebar
categories = create_nav_structure()

def render_sidebar(categories):
    items = []
    for category, subcategories in categories.items():
        subcategory_links = [
            html.A(name, href=link, style={"display": "block", "padding": "5px 10px", "textDecoration": "none", "color": "black"})
            for name, link in subcategories.items()
        ]
        items.append(
            html.Div([
                html.H5(category, style={"marginTop": "10px"}),
                html.Div(subcategory_links, style={"paddingLeft": "10px"})
            ])
        )
    return html.Div(items)

sidebar = html.Div([
    html.H2("Navigation", className="display-4"),
    html.Hr(),
    render_sidebar(categories)
], className="sidebar")

app.layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(sidebar, width=3),
            dbc.Col(html.Div("Inhalt des Dashboards"), width=9)
        ])
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True)
