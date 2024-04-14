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


app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Cards Against Humanity: Future of Democracy and Elections in America",
                        style={'textAlign': 'center', 'color': colors['dark_blue'], 'fontSize': '40px'}))
    ]),
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
