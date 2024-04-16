
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


arturo_rey_info = """Data Scientist with extensive experience in data modeling 
                    using machine learning, business intelligence, and managing 
                    the overall data flow, data processing and modeling process. 
                    Proven ability to develop business solutions by analyzing and 
                    interpreting data to create value."""

salva_umar_info = """SBackground in Computer Science \n
                    Experienced Data Analyst with a focus on traffic analysis and 
                    prediction models \n Enthusiastic about leveraging data science 
                    to tackle practical challenges and drive impactful solutions"""

sampson_yu_info = """Background in Electrical and Computer Engineering \n
                     Experienced Data Scientist and Software Engineer \n
                     Passionate about applying data science to address and 
                     solve real-world problems."""

sophia_zhao_info = """Background in Business Analytics & Accounting \n
                      Experience in conducting data-driven business decision 
                      making in Fin-tech & Retail industries \n Eager to 
                      apply data science skillsets and maximize organizational 
                      efficiency & effectiveness"""


from PIL import Image
pil_image = Image.open("./img/logo.png")

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

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Dashboard", href="#", style={'color': colors['light_blue']})),
        dbc.NavItem(dbc.NavLink("About Us", href="/about-us", style={'color': colors['light_blue']})),
    ],
    brand=html.Div([
        html.Img(src=pil_image, height="40px"),
        "Cards Against Humanity: Future of Democracy and Elections in America"
    ]),
    brand_href="#",
    color=colors['light_grey'],
    dark=True
)

navbar_brand_style = {
    'color': colors['dark_blue'],
    'fontSize':'30px',
    'fontWeight': 'bold',
    'justify':'left',
    'padding-top': '0px'

}


navbar.brand_style = navbar_brand_style


def main_page_layout():
    return html.Div([
        dbc.Container([
        navbar,
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.Label("Age Slider", htmlFor="age-slider",
                                style={'color': colors['white'], 'fontWeight': 'bold', 'fontSize': '20px'}),
                        dcc.RangeSlider(
                            id='age-slider',
                            min=min_age,
                            max=max_age,
                            step=1,
                            value=[min_age, max_age],
                            marks={i: {'label': str(i), 'style': {'color': colors['white']}}
                                for i in range(min_age, max_age + 1, 10)},
                            className='custom-slider'
                        )
                    ])
                ], style={'backgroundColor': colors['dark_blue'], 'borderRadius': '10px', 'boxShadow': '2px 2px 10px #888888'})
            ], width=3),

            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.Label("Racial Group", htmlFor="racial-group-dropdown",
                                style={'color': colors['white'], 'fontWeight': 'bold', 'fontSize': '20px'}),
                        dcc.Dropdown(
                            options=[{'label': range_val, 'value': range_val}
                                    for range_val in race_],
                            value=['White', 'Black'],
                            id="racial-group-dropdown",
                            multi=True,
                        )
                    ])
                ], style={'backgroundColor': colors['dark_blue'], 'borderRadius': '10px', 'boxShadow': '2px 2px 10px #888888'})
            ], width=3),

            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.Label("Political Ideology", htmlFor="ideology-dropdown",
                                style={'color': colors['white'], 'fontWeight': 'bold', 'fontSize': '20px'}),
                        dcc.Dropdown(
                            options=[{'label': range_val, 'value': range_val}
                                    for range_val in ideology_],
                            value=['Conservative', 'Liberal'],
                            id="ideology-dropdown",
                            multi=True
                        )
                    ])
                ], style={'backgroundColor': colors['dark_blue'], 'borderRadius': '10px', 'boxShadow': '2px 2px 10px #888888'})
            ], width=3),

            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.Label("Education", htmlFor="higher-education-dropdown",
                                style={'color': colors['white'], 'fontWeight': 'bold', 'fontSize': '20px'}),
                        dcc.Dropdown(
                            options=[{'label': range_val, 'value': range_val}
                                    for range_val in higher_education_],
                            value=['College degree', 'Some college'],
                            id="higher-education-dropdown",
                            multi=True
                        )
                    ])
                ], style={'backgroundColor': colors['dark_blue'], 'borderRadius': '10px', 'boxShadow': '2px 2px 10px #888888'})
            ], width=3)
        ], justify='around'),  # Space elements evenly across the row

        dbc.Row([
            dbc.Col([
                html.H2("General Correlations", style={
                        'textAlign': 'center',  'color': colors['red'], 'fontSize': '35px'}),
                dbc.Row([
                    dbc.Col(dcc.Graph(id='stacked-chart-race',
                                    figure=stacked_chart_race), md=6),
                    dbc.Col(dcc.Graph(id='stacked-chart-education',
                                    figure=stacked_chart_education), md=6),
                    # Margin for the inner row containing graphs
                ], justify='center', style={'margin': '0px'}),

                dbc.Row(
                    # Assuming war_likelihood_chart_component is defined
                    dcc.Graph(id='war-likelihood-chart',
                            figure=war_likelihood_chart),
                    justify='center',
                    # Added space above this row
                    style={'margin': '0px'}
                ),
            ], md=6),

            dbc.Col([
                html.H2("Elections: Donald Trump Focused",
                        style={'textAlign': 'center', 'color': colors['red'], 'fontSize': '35px'}),
                dbc.Row(
                    dcc.Graph(id='donut-chart', figure=donut_chart_figure),
                    justify='center',  # Center align the graph
                    # Added space below this row
                    style={'margin': '25px'},

                ),
                dbc.Row(
                    dcc.Graph(id='heatmap', figure=heat_map),
                    justify='center',  # Center align the heatmap
                    # Added space above this row
                    style={'margin': '0px'}
                ),
            ], md=6),
        ], style={'marginTop': 5}, justify='center', className='vertical-line-row'),



    ], fluid=True, style={'backgroundColor': colors['light_grey'], 'padding': '20px'})
    ])


# ABOUT US MEMBERS

member_card_arturo = dbc.Card([
    dbc.CardImg(src="member_image.jpg", top=True, style={'height': '200px', 'objectFit': 'cover'}),
    dbc.CardBody([
        html.H5("Arturo Rey Haggar", className="card-title"),
        html.P(arturo_rey_info)
    ])
], style={'margin': '10px'})

member_card_salva = dbc.Card([
    dbc.CardImg(src="member_image.jpg", top=True, style={'height': '200px', 'objectFit': 'cover'}),
    dbc.CardBody([
        html.H5("Salva Umar", className="card-title"),
        html.P(salva_umar_info)
    ])
], style={'margin': '10px'})

member_card_sampson = dbc.Card([
    dbc.CardImg(src="member_image.jpg", top=True, style={'height': '200px', 'objectFit': 'cover'}),
    dbc.CardBody([
        html.H5("Sampson Yu", className="card-title"),
        html.P(sampson_yu_info)
    ])
], style={'margin': '10px'})

member_card_sophia = dbc.Card([
    dbc.CardImg(src="member_image.jpg", top=True, style={'height': '200px', 'objectFit': 'cover'}),
    dbc.CardBody([
        html.H5("Sophia Zhao", className="card-title"),
        html.P(sophia_zhao_info)
    ])
], style={'margin': '10px'})

# About Us page layout with grid
about_us_layout = html.Div([
    dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Dashboard", href="/#", style={'color': colors['light_blue']})),
        dbc.NavItem(dbc.NavLink("About Us", href="/about-us", style={'color': colors['light_blue'],'fontWeight':'light'})),
    ],
    brand=html.Div([
        html.Img(src=pil_image, height="40px"),
        "Cards Against Humanity: Future of Democracy and Elections in America"
    ],style={'color': colors['dark_blue'],'justify':'center'}),
    brand_href="#",
    color=colors['light_grey'],
    dark=True,
    style = navbar_brand_style),
    dbc.Container([
        html.H1("About Us"),
        dbc.Row([
            dbc.Col(member_card_arturo, width=6),
            dbc.Col(member_card_salva, width=6)
        ]),
        dbc.Row([
            dbc.Col(member_card_sampson, width=6),
            dbc.Col(member_card_sophia, width=6)
        ])
    ], className="mt-4", fluid=True, style={'backgroundColor': colors['light_grey'], 'paddingTop': '-50px', 'padding-bot': '50px'})
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
