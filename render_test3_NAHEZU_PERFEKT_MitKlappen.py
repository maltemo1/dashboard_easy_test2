import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Kategorien und Subkategorien mit Links für zukünftige Navigation
def create_nav_structure():
    return {
        "Überblick über Deutschlands Handel": {
            "Gesamtüberblick seit 2008 bis 2024": {
                "Gesamter Export-, Import- und Handelsvolumen-Verlauf Deutschlands": "#"
            },
            "Überblick nach bestimmtem Jahr": {
                "Monatlicher Handelsverlauf": "#",
                "Top 10 Handelspartner": "#",
                "Länder mit größten Export- und Importzuwächsen (absolut)": "#",
                "Länder mit größten Export- und Importzuwächsen (relativ)": "#",
                "Top 10 Waren": "#",
                "Waren mit größten Export- und Importzuwächsen (absolut)": "#",
                "Waren mit größten Export- und Importzuwächsen (relativ)": "#",
            }
        },
        "Länderanalyse": {
            "Gesamtüberblick seit 2008 bis 2024": {
                "Gesamter Export-, Import- und Handelsvolumen-Verlauf": "#",
                "Vergleich mit anderen Ländern": "#",
                "Export- und Importwachstumsrate": "#",
                "Platzierung im Ranking": "#",
                "Deutschlands Top 10 Waren im Handel": "#",
            },
            "Überblick nach bestimmtem Jahr": {
                "Handelsbilanz & Ranking": "#",
                "Monatlicher Handelsverlauf": "#",
                "Top 10 Export- und Importwaren": "#",
                "Top 4 Waren nach Differenz zum Vorjahr": "#",
                "Top 4 Waren nach Wachstum zum Vorjahr": "#",
            },
            "Überblick nach bestimmter Ware": {
                "Gesamter Export- und Importverlauf": "#"
            },
            "Überblick nach bestimmtem Jahr und Ware": {
                "Monatlicher Verlauf von Export und Import": "#"
            },
            "Überblick nach bestimmtem Zeitraum und Waren": {
                "Jährlicher Export- und Importverlauf für ein Land": "#",
                "Jährlicher Export- und Importverlauf für eine Ware": "#",
            }
        },
        "Warenanalyse": {
            "Gesamtüberblick seit 2008 bis 2024": {
                "Gesamter Export- und Importverlauf": "#",
                "Top 5 Export- und Importländer": "#",
            },
            "Überblick mit mehreren Waren über bestimmten Zeitraum": {
                "Jährliche Werte": "#",
                "Monatliche Werte": "#",
            },
            "Überblick nach bestimmtem Jahr": {
                "Ranking der Ware": "#",
                "Monatlicher Handelsverlauf": "#",
            },
            "Überblick nach bestimmtem Land": {
                "Gesamter Export- und Importverlauf für ein Land": "#",
            },
            "Überblick nach bestimmtem Zeitraum und Land und Waren": {
                "Jährlicher Verlauf für mehrere Waren in einem Land": "#",
                "Jährlicher Verlauf für eine Ware in mehreren Ländern": "#",
            }
        }
    }

# Funktion zum Rendern der Sidebar
categories = create_nav_structure()

def render_sidebar(categories):
    def create_items(subcategories):
        items = []
        for name, value in subcategories.items():
            if isinstance(value, dict):
                items.append(
                    dbc.AccordionItem(
                        dbc.Accordion(create_items(value), start_collapsed=True),
                        title=name
                    )
                )
            else:
                items.append(
                    dbc.AccordionItem(
                        html.A(name, href=value, style={"textDecoration": "none", "color": "black"}),
                        title=name
                    )
                )
        return items
    
    return dbc.Accordion([
        dbc.AccordionItem(
            dbc.Accordion(create_items(subcategories), start_collapsed=True),
            title=category
        )
        for category, subcategories in categories.items()
    ], start_collapsed=True)

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
