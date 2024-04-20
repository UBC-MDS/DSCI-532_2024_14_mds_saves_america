from PIL import Image
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd
import altair as alt
import plotly.express as px
from dash.dependencies import Input, Output
from dash import dash_table
from src.callbacks import update_donut_chart, update_stacked_chart_race, update_stacked_chart_education, update_heatmap_data, update_war_likelihood_chart, update_slider_marks

from dash import Dash
from dash.dependencies import Input, Output

from src.data import df, df_pct, df_pct_education, min_age, max_age, race_, ideology_, higher_education_
from src.components import create_donut_chart, create_stacked_chart_race, create_stacked_chart_education, create_war_likelihood_chart, create_heatmap


# Initialize the app
app = Dash(__name__,
           external_stylesheets=['https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css'])
server = app.server


arturo_rey_info = """Data Scientist with 3 years of experience."""

salva_umar_info = """Background in Computer Science. 
Experienced Data Analyst with a focus on traffic analysis and prediction models. 
Enthusiastic about leveraging data science to tackle practical challenges and drive impactful solutions.
"""

sampson_yu_info = """Background in Electrical and Computer Engineering.
Experienced Data Scientist and Software Engineer.
Passionate about applying data science to address and solve real-world problems."""

sophia_zhao_info = """Background in Business Analytics & Accounting.
Experience in conducting data-driven business decision making in Fin-tech & Retail industries.
Eager to apply data science skillsets and maximize organizational efficiency & effectiveness.
"""


pil_image = Image.open("../img/logo.png") # change it back to start with ../ before pushing

# Use the function to create the figure
donut_chart_figure = create_donut_chart(df)
stacked_chart_race = create_stacked_chart_race(df_pct)
stacked_chart_education = create_stacked_chart_education(df_pct_education)
war_likelihood_chart = create_war_likelihood_chart(df)
heat_map = create_heatmap(df)


# Donut chart component
donut_chart_component = dcc.Graph(
    id='donut-chart',
    figure=donut_chart_figure
)

stacked_chart_component_race = dcc.Graph(
    id='stacked-chart-race',
    figure=stacked_chart_race
)

stacked_chart_component_education = dcc.Graph(
    id='stacked-chart-education',
    figure=stacked_chart_education
)

war_likelihood_chart_component = dcc.Graph(
    id='war-likelihood-chart',
    figure=war_likelihood_chart
)
heatmap_component = dcc.Graph(
    id='heatmap',
    figure=heat_map
)

colors = {'light_blue': '#0d76bd',
          'dark_blue': '#0660a9',
          'red': '#ed1c23',
          'white': '#ffffff',
          'grey': '#888888',
          'light_grey': '#d3d3d3'
          }


# Navbar part

navbar = dbc.Navbar(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Img(src=pil_image, height="40px"),
                    width="auto"
                ),
                dbc.Col(
                    html.Span("Cards Against Humanity: Future of Democracy and Elections in America", style={
                              'color': colors['dark_blue'], 'fontSize': '35px', 'fontWeight': 'bold'}),
                    width=True
                ),
                dbc.Col(
                    dbc.Nav(
                        [
                            dbc.NavItem(dbc.NavLink("Dashboard", href="#", style={
                                        'color': colors['light_blue'], 'fontSize': '18px', 'fontWeight': 'bold'})),
                            dbc.NavItem(dbc.NavLink("About Us", href="/about-us", style={
                                        'color': colors['light_blue'], 'fontSize': '18px', 'fontWeight': 'bold'}))
                        ],
                        navbar=True,
                        className="ml-auto"
                    ),
                    width="auto",
                    style={'marginLeft': '0px'}
                )
            ], style={'marginLeft': 90}, justify='right', align='center'
        )
    ],
    color=colors['light_grey'],
    dark=True,
    style={'height': '40px', 'paddingLeft': '10px', 'paddingRight': '0px'}
)


navbar_brand_style = {
    'color': colors['dark_blue'],
    'fontSize': '24px',
    'fontWeight': 'bold',
    'justify': 'center',
    'padding-top': '0px'
}
navbar.brand_style = navbar_brand_style


def main_page_layout():
    return html.Div([
        html.Link(rel='icon', href='./assets/favicon.ico'),
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    navbar
                ], style={'marginBottom': '5px'})
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Label("Age Slider", htmlFor="age-slider",
                                       style={'color': colors['white'], 'fontWeight': 'bold', 'fontSize': '15px'}),
                            dcc.RangeSlider(
                                id='age-slider',
                                min=min_age,
                                max=max_age,
                                step=1,
                                value=[25, 65],
                                marks={i: {'label': str(i), 'style': {'color': colors['white']}}
                                       for i in range(min_age, max_age + 1, 10)},
                                className='custom-slider'
                            )
                        ])
                    ], style={'backgroundColor': colors['dark_blue'], 'borderRadius': '10px', 'boxShadow': '2px 2px 10px #888888', 'marginBottom': '8px'})
                ], width=3),

                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Label("Racial Group", htmlFor="racial-group-dropdown",
                                       style={'color': colors['white'], 'fontWeight': 'bold', 'fontSize': '15px'}),
                            dcc.Dropdown(
                                options=[{'label': range_val, 'value': range_val}
                                         for range_val in race_],
                                value=['White', 'Black'],
                                id="racial-group-dropdown",
                                placeholder="Select an option",
                                multi=True,
                            )
                        ])
                    ], style={'backgroundColor': colors['dark_blue'], 'borderRadius': '10px', 'boxShadow': '2px 2px 10px #888888', 'marginBottom': '8px'})
                ], width=3),

                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Label("Political Ideology", htmlFor="ideology-dropdown",
                                       style={'color': colors['white'], 'fontWeight': 'bold', 'fontSize': '15px'}),
                            dcc.Dropdown(
                                options=[{'label': range_val, 'value': range_val}
                                         for range_val in ideology_],
                                value=['Conservative', 'Liberal'],
                                placeholder="Select an option",
                                id="ideology-dropdown",
                                multi=True
                            )
                        ])
                    ], style={'backgroundColor': colors['dark_blue'], 'borderRadius': '10px', 'boxShadow': '2px 2px 10px #888888', 'marginBottom': '8px'})
                ], width=3),

                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Label("Education", htmlFor="higher-education-dropdown",
                                       style={'color': colors['white'], 'fontWeight': 'bold', 'fontSize': '15px'}),
                            dcc.Dropdown(
                                options=[{'label': range_val, 'value': range_val}
                                         for range_val in higher_education_],
                                value=['College degree', 'Some college'],
                                placeholder="Select an option",
                                id="higher-education-dropdown",
                                multi=True
                            )
                        ])
                    ], style={'backgroundColor': colors['dark_blue'], 'borderRadius': '10px', 'boxShadow': '2px 2px 10px #888888', 'marginBottom': '8px'})
                ], width=3)
            ], justify='around'),

            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("General Correlations", style={
                                       'textAlign': 'center', 'color': colors['red'], 'fontSize': '25px'}),
                        dbc.CardBody([
                            dbc.Row([
                                dbc.Col(dcc.Graph(id='stacked-chart-race',
                                                  figure=stacked_chart_race), md=6),
                                dbc.Col(dcc.Graph(id='stacked-chart-education',
                                                  figure=stacked_chart_education), md=6)
                            ], class_name='align-items-stretch'),
                            dcc.Graph(id='war-likelihood-chart',
                                      figure=war_likelihood_chart)
                        ])
                    ], style={'backgroundColor': colors['light_grey'], 'borderRadius': '10px'})
                ], md=6),

                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Elections: Donald Trump Focused", style={
                                       'textAlign': 'center', 'color': colors['red'], 'fontSize': '25px'}),
                        dbc.CardBody([
                            dcc.Graph(id='heatmap', figure=heat_map),
                                      html.Div([
                                        html.H6("Voting Fairness", style={'display': 'inline-block', 'margin-right': '5px', 'color':colors['light_blue']}), 
                                        html.Abbr("\u2139", title="Voting Fairness refers to whether or not Americans think votes are counted fairly in American elections.", 
                                                style={'text-decoration': 'none', 'cursor': 'help'})
                                            ]),
                            dcc.Graph(id='donut-chart',
                                      figure=donut_chart_figure)
                        ])

                    ], style={'backgroundColor': colors['light_grey'], 'borderRadius': '10px'})
                ], md=6)
            ], justify='center', class_name='align-items-stretch')
        ], fluid=True, style={'backgroundColor': colors['light_grey'], 'padding': '20px'}),
        html.P("Please note that the color schemes used across different visual components in this application are independent and may vary.", 
           style={'font-size': '12px', 'color': colors['light_blue'], 'backgroundColor': colors['light_grey']})
    ])


# ABOUT US MEMBERS
member_card_arturo = dbc.Card([
    dbc.CardImg(src="member_image.jpg", top=True, style={
                'height': '200px', 'objectFit': 'cover'}),
    dbc.CardBody([
        html.H5("Arturo Rey Haggar", className="card-title"),
        html.P(arturo_rey_info)
    ])
], style={'margin': '10px'})

member_card_salva = dbc.Card([
    dbc.CardImg(src="member_image.jpg", top=True, style={
                'height': '200px', 'objectFit': 'cover'}),
    dbc.CardBody([
        html.H5("Salva Umar", className="card-title"),
        html.P(salva_umar_info)
    ])
], style={'margin': '10px'})

member_card_sampson = dbc.Card([
    dbc.CardImg(src="member_image.jpg", top=True, style={
                'height': '200px', 'objectFit': 'cover'}),
    dbc.CardBody([
        html.H5("Sampson Yu", className="card-title"),
        html.P(sampson_yu_info)
    ])
], style={'margin': '10px'})

member_card_sophia = dbc.Card([
    dbc.CardImg(src="member_image.jpg", top=True, style={
                'height': '200px', 'objectFit': 'cover'}),
    dbc.CardBody([
        html.H5("Sophia Zhao", className="card-title"),
        html.P(sophia_zhao_info)
    ])
], style={'margin': '10px'})

# About Us page layout with grid
about_us_layout = html.Div([
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Dashboard", href="/#",
                        style={'color': colors['light_blue'], 'fontSize': '20px'})),
            dbc.NavItem(dbc.NavLink("About Us", href="/about-us", style={
                        'color': colors['light_blue'], 'fontSize': '20px', 'fontWeight': 'light'})),
        ],
        brand=html.Div([
            html.Img(src=pil_image, height="40px",
                     style={'marginRight': '15px'}),
            "Cards Against Humanity: Future of Democracy and Elections in America"
        ], style={'color': colors['dark_blue'], 'justify': 'center', 'fontSize': '24px', 'display': 'flex', 'alignItems': 'center'}),
        brand_href="#",
        color=colors['light_grey'],
        dark=True,
        style=navbar_brand_style
    ),
    dbc.Container([
        html.H1("About Us", style={'marginTop': '20px'}),
        dbc.Row([
            dbc.Col(member_card_arturo, width=6),
            dbc.Col(member_card_salva, width=6)
        ]),
        dbc.Row([
            dbc.Col(member_card_sampson, width=6),
            dbc.Col(member_card_sophia, width=6)
        ])
    ], className="mt-4")
])


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/about-us':
        return about_us_layout
    else:
        return main_page_layout()


# Link the callbacks
app.callback(
    Output('donut-chart', 'figure'),
    [Input('age-slider', 'value'),
     Input('higher-education-dropdown', 'value'),
     Input('ideology-dropdown', 'value'),
     Input('racial-group-dropdown', 'value')]
)(update_donut_chart)

app.callback(
    Output('stacked-chart-race', 'figure'),
    [Input('age-slider', 'value'),
     Input('higher-education-dropdown', 'value'),
     Input('ideology-dropdown', 'value'),
     Input('racial-group-dropdown', 'value')]
)(update_stacked_chart_race)

app.callback(
    Output('stacked-chart-education', 'figure'),
    [Input('age-slider', 'value'),
     Input('higher-education-dropdown', 'value'),
     Input('ideology-dropdown', 'value'),
     Input('racial-group-dropdown', 'value')]
)(update_stacked_chart_education)

app.callback(
    Output('heatmap', 'figure'),
    [Input('age-slider', 'value'),
     Input('higher-education-dropdown', 'value'),
     Input('ideology-dropdown', 'value'),
     Input('racial-group-dropdown', 'value')]
)(update_heatmap_data)

app.callback(
    Output('war-likelihood-chart', 'figure'),
    [Input('age-slider', 'value'),
     Input('higher-education-dropdown', 'value'),
     Input('ideology-dropdown', 'value'),
     Input('racial-group-dropdown', 'value')]
)(update_war_likelihood_chart)

app.callback(
    Output('age-slider', 'marks'),
    [Input('age-slider', 'value')]
)(update_slider_marks)


if __name__ == '__main__':
    app.run()
