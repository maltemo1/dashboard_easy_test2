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
            }
        },
        "Warenanalyse": {
            "Gesamtüberblick seit 2008 bis 2024": {
                "Gesamter Export- und Importverlauf": "#",
                "Top 5 Export- und Importländer": "#",
            }
        }
    }

# Funktion zum Rendern der Sidebar
categories = create_nav_structure()

def render_sidebar(categories):
    def create_items(subcategories):
        items = []
        for name, value in subcategories.items():
            if isinstance(value, dict):  # Falls weitere Unterkategorien existieren
                sub_items = [
                    html.A(sub_name, href=sub_value, style={"textDecoration": "none", "color": "black", "paddingLeft": "10px"})
                    for sub_name, sub_value in value.items()
                ]
                items.append(
                    dbc.AccordionItem(
                        html.Div(sub_items),
                        title=name
                    )
                )
            else:  # Falls es sich um eine klickbare Subkategorie handelt
                items.append(
                    html.A(name, href=value, style={"textDecoration": "none", "color": "black", "display": "block", "padding": "5px 10px"})
                )
        return items
    
    return dbc.Accordion([
        dbc.AccordionItem(
            html.Div(create_items(subcategories)),
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
