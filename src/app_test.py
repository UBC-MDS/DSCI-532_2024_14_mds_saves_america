from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd
import altair as alt
import plotly.express as px

# Initialize the app
app = Dash(__name__, 
external_stylesheets=['https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css'])

colors = {'light_blue': '#0d76bd',
          'dark_blue': '#0660a9',
          'red': '#ed1c23',
          'white': '#ffffff',
          'grey': '#888888',
          'light_grey': '#d3d3d3'
          }

df = pd.read_csv("data/processed/data_cleaned.csv")

age_range_ = df['age_range'].unique().tolist()
race_ = df['race'].unique().tolist()
ideology_ = df['ideology'].unique().tolist()
higher_education_ = df['higher_education'].unique().tolist()

min_age = df['age'].min()
max_age = df['age'].max()

df_pct = df.groupby(['race', 'political_party']).size().unstack(fill_value=0).apply(lambda x: x / x.sum(), axis=1).stack().reset_index(name='percentage')
df_pct_education = df.groupby(['higher_education', 'political_party']).size().unstack(fill_value=0).apply(lambda x: x / x.sum(), axis=1).stack().reset_index(name='percentage')


race_pol_party_chart1 = alt.Chart(df_pct).mark_bar().encode(
    x=alt.X('race', axis=alt.Axis(title='Race')),
    y=alt.Y('percentage:Q', axis=alt.Axis(format='%'), stack='normalize', title='Percentage'),
    color=alt.Color('political_party', legend=alt.Legend(title='Political Party'))
).properties(
    title='100% Stacked Bar Chart of Political Party by Race'
)


def create_stacked_chart_race(df):
    party_colors = {'Republican': colors['red'], 
                    'Democrat': colors['dark_blue'], 
                    'DK/REF': colors['white'], 
                    'Independent': colors['light_blue']}

    fig = px.bar(df, x='race', y='percentage', color='political_party',
             title='Stacked Bar Chart of Political Party by Race',
             labels={'percentage': 'Percentage', 'race': 'Race'},
             category_orders={'race': sorted(df['race'].unique())},
             hover_data={'percentage': ':.2%'},
             barmode='relative',
             color_discrete_map=party_colors)

    fig.update_yaxes(title='Percentage', tickformat='%')
    fig.update_layout(
        {
        "paper_bgcolor": colors['light_grey'],
        "plot_bgcolor": colors['light_grey'],
        },
        legend_title='Political Party',
    )

    return fig


def create_stacked_chart_education(df):
    party_colors = {'Republican': colors['red'], 
                    'Democrat': colors['dark_blue'], 
                    'DK/REF': colors['white'], 
                    'Independent': colors['light_blue']}

    fig = px.bar(df, x='higher_education', y='percentage', color='political_party',
             title='Stacked Bar Chart of Political Party by Highest Education',
             labels={'percentage': 'Percentage', 'higher_education': 'Higher Education'},
             category_orders={'higher_education': sorted(df['higher_education'].unique())},
             hover_data={'percentage': ':.2%'},
             barmode='relative',
             color_discrete_map=party_colors)

    fig.update_yaxes(title='Percentage', tickformat='%')
    fig.update_layout(
        {
        "paper_bgcolor": colors['light_grey'],
        "plot_bgcolor": colors['light_grey'],
        },
        legend_title='Political Party',
    )

    return fig

def create_donut_chart(df):
     # Calculate the counts for each category in the 'trump_2020' column
     counts = df['trump_2020'].value_counts().reset_index()
     counts.columns = ['trump_2020', 'counts']


     # Create the pie chart with a hole (donut chart)
     fig_donut = px.pie(counts, values='counts', names='trump_2020', hole=0.4)

     # Update the layout and trace for the donut chart appearance
     fig_donut.update_traces(textinfo='percent+label', pull=[0.1 if i == 0 else 0 for i in range(len(counts))],
                            marker=dict(colors=list(colors.values())[:len(df['trump_2020'].unique())]))
     fig_donut.update_layout(
        {
        "paper_bgcolor": colors['light_grey'],
        "plot_bgcolor": colors['light_grey'],
        },
        title='Likelihood of Donald Trump Reelection in 2020',
        showlegend=True,
        annotations=[dict(text='Trump', x=0.5, y=0.5, font_size=20, showarrow=False)],
        plot_bgcolor=colors['light_grey'],
        

        
     )
     return fig_donut

 # Use the function to create the figure for the initial state of the donut chart
donut_chart_figure = create_donut_chart(df)

stacked_chart_race = create_stacked_chart_race(df_pct)

stacked_chart_education = create_stacked_chart_education(df_pct_education)

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



app.layout = html.Div([

    dbc.Row([
        dbc.Col([
            html.H1("Cards Against Humanity: Future of Democracy and Elections in America", style={'textAlign': 'center','color': '#0660a9', 'fontSize':'24px'}),
            dbc.Row([
                dbc.Col([
                    html.Label("Age Range", htmlFor="state-dropdown1",style={'color':colors['white']}),
                     dcc.RangeSlider(
                                    id='age-slider',
                                    min=min_age,
                                    max=max_age,
                                    step=1,
                                    value=[min_age, max_age],
                                    marks={i: str(i) for i in range(min_age, max_age + 1, 10)}
                                    ),
                ]), 
                dbc.Col([
                    html.Label("Racial Group", htmlFor="racial-group-dropdown",style={'color':colors['white']}),
                    dcc.Dropdown(
                        options=[{'label': range_val, 'value': range_val} for range_val in race_],  #pass the age here
                        value=race_[0],
                        id="racial-group-dropdown"),
                ]),
                dbc.Col([
                    html.Label("Political Ideology", htmlFor="ideology-dropdown",style={'color':colors['white']}),
                    dcc.Dropdown(
                        options=[{'label': range_val, 'value': range_val} for range_val in ideology_],  #pass the age here
                        value=ideology_[0],
                        id="ideology-dropdown"),
                ]),
                dbc.Col([
                    html.Label("Level of Higher Education", htmlFor="higher-education-dropdown",style={'color':colors['white']}),
                    dcc.Dropdown(
                        options=[{'label': range_val, 'value': range_val} for range_val in higher_education_],  #pass the age here
                        value=higher_education_[0],
                        id="higher-education-dropdown"),
                ]),
                html.Br(),    
            ], style={'backgroundColor': colors['light_blue'], 'width': '100%', 'margin-left': '0px', 'margin-right': '0px'}),
            dbc.Row(html.Div(style={'height': '10px', 'background-color': colors['light_blue'],'width': '100%', 'margin-left': '0px', 'margin-right': '0px'}))
        ])
    ]),
    dbc.Row([
        html.Br(),  # Add whitespace; br = "break",
        html.Br(),  # Add whitespace; br = "break",
        dbc.Col(dcc.Graph(id='stacked-chart-race',figure=stacked_chart_race)),
        dbc.Col(dcc.Graph(id='stacked-chart-education',figure=stacked_chart_education)),
        dbc.Col(dcc.Graph(id='donut-chart', figure=donut_chart_figure)),
    ],style={'backgroundColor': colors['light_grey']}),
])

app.layout = html.Div([
    html.Link(
        href='https://stackpath.bootstrapcdn.com/bootstrap/5.3.2/css/bootstrap.min.css',
        rel='stylesheet'
    ),
    html.Div(
        app.layout,
        style={'backgroundColor': colors['light_grey']}
    )
])


@app.callback(
     Output('donut-chart', 'figure'),
     [Input('age-slider', 'value'),
     Input('higher-education-dropdown','value'),
     Input('ideology-dropdown', 'value'),
     Input('racial-group-dropdown','value')]
 )

def update_donut_chart(age_range,
                       education,
                       ideology,
                       race):
    filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]
    filtered_df = filtered_df[filtered_df['higher_education'] == education]
    filtered_df = filtered_df[filtered_df['ideology'] == ideology]
    filtered_df = filtered_df[filtered_df['race'] == race]


    return create_donut_chart(filtered_df)


@app.callback(
     Output('stacked-chart-race', 'figure'),
     [Input('age-slider', 'value'),
     Input('higher-education-dropdown','value'),
     Input('ideology-dropdown', 'value'),
     Input('racial-group-dropdown','value')]
 )

def update_stacked_chart_race(age_range,
                       education,
                       ideology,
                       race):
    filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]
    filtered_df = filtered_df[filtered_df['higher_education'] == education]
    filtered_df = filtered_df[filtered_df['ideology'] == ideology]
    filtered_df = filtered_df[filtered_df['race'] == race]

    df_pct = filtered_df.groupby(['race', 'political_party']).size().unstack(fill_value=0).apply(lambda x: x / x.sum(), axis=1).stack().reset_index(name='percentage')

    return create_stacked_chart_race(df_pct)



@app.callback(
     Output('stacked-chart-education', 'figure'),
     [Input('age-slider', 'value'),
     Input('higher-education-dropdown','value'),
     Input('ideology-dropdown', 'value'),
     Input('racial-group-dropdown','value')]
 )

def update_stacked_chart_education(age_range,
                       education,
                       ideology,
                       race):
    filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]
    filtered_df = filtered_df[filtered_df['higher_education'] == education]
    filtered_df = filtered_df[filtered_df['ideology'] == ideology]
    filtered_df = filtered_df[filtered_df['race'] == race]

    df_pct = filtered_df.groupby(['higher_education', 'political_party']).size().unstack(fill_value=0).apply(lambda x: x / x.sum(), axis=1).stack().reset_index(name='percentage')

    return create_stacked_chart_education(df_pct)

if __name__ == '__main__':
    app.run_server(debug=True)



