from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd
import altair as alt
import plotly.express as px
from dash.dependencies import Input, Output
from dash import dash_table
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

df_pct = df.groupby(['race', 'political_party']).size().unstack(fill_value=0).apply(
    lambda x: x / x.sum(), axis=1).stack().reset_index(name='percentage')
df_pct_education = df.groupby(['higher_education', 'political_party']).size().unstack(
    fill_value=0).apply(lambda x: x / x.sum(), axis=1).stack().reset_index(name='percentage')


race_pol_party_chart1 = alt.Chart(df_pct).mark_bar().encode(
    x=alt.X('race', axis=alt.Axis(title='Race')),
    y=alt.Y('percentage:Q', axis=alt.Axis(format='%'),
            stack='normalize', title='Percentage'),
    color=alt.Color('political_party', legend=alt.Legend(
        title='Political Party'))
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
                 labels={'percentage': 'Percentage',
                         'higher_education': 'Higher Education'},
                 category_orders={'higher_education': sorted(
                     df['higher_education'].unique())},
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
        annotations=[dict(text='Trump', x=0.5, y=0.5,
                          font_size=20, showarrow=False)],
        plot_bgcolor=colors['light_grey'],



    )
    return fig_donut


def create_war_likelihood_chart(df):
    # Define colors for the opinions to match the American flag theme
    opinion_colors = {'Very Likely': colors['red'],
                      'Somewhat Likely': colors['white'],
                      'Not at all likely': colors['dark_blue']}

    # Map the numeric values to string categories if they represent categorical data
    likelihood_mapping = {0: 'Not at all likely',
                          1: 'Somewhat Likely', 2: 'Very Likely'}
    df['likelihood_of_war'] = df['likelihood_of_war'].map(likelihood_mapping)

    # Aggregate the data to get the count of responses for each category
    likelihood_counts = df['likelihood_of_war'].value_counts().reset_index()
    likelihood_counts.columns = ['Opinion', 'Count']

    # Sort the dataframe based on the opinion order you want in the chart
    ordered_opinions = ['Very Likely', 'Somewhat Likely', 'Not at all likely']
    likelihood_counts['Opinion'] = pd.Categorical(
        likelihood_counts['Opinion'], categories=ordered_opinions, ordered=True)
    likelihood_counts = likelihood_counts.sort_values('Opinion')

    # Create the horizontal bar chart using Plotly Express
    fig = px.bar(likelihood_counts, y='Opinion', x='Count',
                 title='Perceived Likelihood of War',
                 labels={'Count': 'Number of Responses',
                         'Opinion': 'Opinion on Likelihood of War'},
                 text='Count', orientation='h',
                 color='Opinion',
                 color_discrete_map=opinion_colors)

    fig.update_layout(
        {
            "paper_bgcolor": colors['light_grey'],
            "plot_bgcolor": colors['light_grey'],
        }
    )
    return fig

table_component = html.Div(
    dash_table.DataTable(
        id='approval-fairness-table',
        columns=[
            {"name": "Trump Approval", "id": "trump_approval"},
            {"name": "DK/REF", "id": "DK/REF"},
            {"name": "No", "id": "No"},
            {"name": "Yes, somewhat confident", "id": "Yes, somewhat confident"},
            {"name": "Yes, very confident", "id": "Yes, very confident"}
        ],
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }
        ],
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        },
        style_cell={
            'whiteSpace': 'normal',
            'height': 'auto',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
            'maxWidth': 0,
        },
        style_table={
            'overflowX': 'auto'  # Enable horizontal scrolling if table exceeds container width
        },
    ),
    style={'overflowX': 'auto'}  # Ensure horizontal scrolling is enabled for the container
)





 # Use the function to create the figure
donut_chart_figure = create_donut_chart(df)
stacked_chart_race = create_stacked_chart_race(df_pct)
stacked_chart_education = create_stacked_chart_education(df_pct_education)
war_likelihood_chart = create_war_likelihood_chart(df)

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

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="/page-1", style={'color': colors['light_blue']})),
        dbc.NavItem(dbc.NavLink("Page 2", href="/page-2", style={'color': colors['light_blue']})),
    ],
    color='0660a9',
    dark=True
)

navbar_brand_style = {
    'color': colors['light_blue'],
    'fontSize':'24px'
}

app.layout = html.Div([
    html.Link(
        href='https://stackpath.bootstrapcdn.com/bootstrap/5.3.2/css/bootstrap.min.css',
        rel='stylesheet'
    ),
    # Header Row with title and filters
    dbc.Row([
        dbc.Col(html.H1("Cards Against Humanity: Future of Democracy and Elections in America",
                        style={'textAlign': 'center', 'color': '#0660a9', 'fontSize': '24px'}))
    ]),

    # Filters row
    dbc.Row([
        dbc.Col(html.Label("Age Range", htmlFor="age-slider",
                style={'color': colors['white']}), width=1),
        dbc.Col(dcc.RangeSlider(id='age-slider', min=min_age, max=max_age, step=1, value=[min_age, max_age],
                                marks={i: str(i) for i in range(min_age, max_age + 1, 10)}), width=10),
    ], style={'backgroundColor': colors['light_blue'], 'padding': '10px'}),

    dbc.Row([
        dbc.Col(html.Label("Racial Group", htmlFor="racial-group-dropdown",
                style={'color': colors['white']}), width=1),
        dbc.Col(dcc.Dropdown(options=[{'label': range_val, 'value': range_val} for range_val in race_],
                             value=['White', 'Black'], id="racial-group-dropdown", multi=True), width=2),
        dbc.Col(html.Label("Political Ideology", htmlFor="ideology-dropdown",
                style={'color': colors['white']}), width=1),
        dbc.Col(dcc.Dropdown(options=[{'label': range_val, 'value': range_val} for range_val in ideology_],
                             value=['Conservative', 'Liberal'], id="ideology-dropdown", multi=True), width=2),
        dbc.Col(html.Label("Level of Higher Education",
                htmlFor="higher-education-dropdown", style={'color': colors['white']}), width=2),
        dbc.Col(dcc.Dropdown(options=[{'label': range_val, 'value': range_val} for range_val in higher_education_],
                             value=['College degree', 'Some college'], id="higher-education-dropdown", multi=True), width=2),
    ], style={'backgroundColor': colors['light_blue'], 'padding': '10px'}),

    # Main content row with two columns for the two main sections
    dbc.Row([
        # Column for "General Correlations" with both charts side by side
        dbc.Col([
            html.H2("General Correlations", style={'textAlign': 'center'}),
            dbc.Row([
                dbc.Col(dcc.Graph(id='stacked-chart-race',
                        figure=stacked_chart_race), md=6),
                dbc.Col(dcc.Graph(id='stacked-chart-education',
                        figure=stacked_chart_education), md=6),
            ]),
            dbc.Row(war_likelihood_chart_component),
        ], md=6),

        # Column for "Elections: Donald Trump Focused"
        dbc.Col([
            html.H2("Elections: Donald Trump Focused",
                    style={'textAlign': 'center'}),
            dbc.Row(dcc.Graph(id='donut-chart', figure=donut_chart_figure)),
            dbc.Row(table_component),
        ], md=6),
    ], style={'marginTop': 30}),
], style={'backgroundColor': colors['light_grey']})


@app.callback(
    Output('donut-chart', 'figure'),
    [Input('age-slider', 'value'),
     Input('higher-education-dropdown', 'value'),
     Input('ideology-dropdown', 'value'),
     Input('racial-group-dropdown', 'value')]
)
def update_donut_chart(age_range,
                       education,
                       ideology,
                       race):
    filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]
    filtered_df = filtered_df[filtered_df['higher_education'].isin(education)]
    filtered_df = filtered_df[filtered_df['ideology'].isin(ideology)]
    filtered_df = filtered_df[filtered_df['race'].isin(race)]

    return create_donut_chart(filtered_df)


@app.callback(
    Output('stacked-chart-race', 'figure'),
    [Input('age-slider', 'value'),
     Input('higher-education-dropdown', 'value'),
     Input('ideology-dropdown', 'value'),
     Input('racial-group-dropdown', 'value')]
)
def update_stacked_chart_race(age_range,
                              education,
                              ideology,
                              race):
    filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]
    filtered_df = filtered_df[filtered_df['higher_education'].isin(education)]
    filtered_df = filtered_df[filtered_df['ideology'].isin(ideology)]
    filtered_df = filtered_df[filtered_df['race'].isin(race)]

    df_pct = filtered_df.groupby(['race', 'political_party']).size().unstack(
        fill_value=0).apply(lambda x: x / x.sum(), axis=1).stack().reset_index(name='percentage')

    return create_stacked_chart_race(df_pct)


@app.callback(
    Output('stacked-chart-education', 'figure'),
    [Input('age-slider', 'value'),
     Input('higher-education-dropdown', 'value'),
     Input('ideology-dropdown', 'value'),
     Input('racial-group-dropdown', 'value')]
)
def update_stacked_chart_education(age_range,
                                   education,
                                   ideology,
                                   race):
    filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]
    filtered_df = filtered_df[filtered_df['higher_education'].isin(education)]
    filtered_df = filtered_df[filtered_df['ideology'].isin(ideology)]
    filtered_df = filtered_df[filtered_df['race'].isin(race)]

    df_pct = filtered_df.groupby(['higher_education', 'political_party']).size().unstack(
        fill_value=0).apply(lambda x: x / x.sum(), axis=1).stack().reset_index(name='percentage')

    return create_stacked_chart_education(df_pct)


@app.callback(
    Output('approval-fairness-table', 'data'),
    [Input('age-slider', 'value'),
     Input('higher-education-dropdown', 'value'),
     Input('ideology-dropdown', 'value'),
     Input('racial-group-dropdown', 'value')]
)
def update_table_data(age_range, education, ideology, race):
    filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]
    filtered_df = filtered_df[filtered_df['higher_education'].isin(education)]
    filtered_df = filtered_df[filtered_df['ideology'].isin(ideology)]
    filtered_df = filtered_df[filtered_df['race'].isin(race)]

    # Pivot the DataFrame to get the counts for each combination of 'trump_approval' and 'fairness_voting'
    pivot_df = filtered_df.pivot_table(index='trump_approval', columns='fairness_voting', aggfunc='size', fill_value=0)
    pivot_df.reset_index(inplace=True)

    # Convert pivot_df to a format suitable for DataTable
    data = pivot_df.to_dict('records')
    print(data)
    return data

if __name__ == '__main__':
    app.run_server(debug=True)