import plotly.express as px
from dash import dash_table
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc


colors = {'light_blue': '#0d76bd',
          'dark_blue': '#0660a9',
          'red': '#ed1c23',
          'white': '#ffffff',
          'grey': '#888888',
          'light_grey': '#d3d3d3'
          }

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

table_component = html.Div([
    html.P("Americans' approval of Donald Trump vs Public opinion on whether Elections are fair",
           style={ 'fontSize': '18px'}),
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
            'backgroundColor': colors['light_blue'],
            'fontWeight': 'bold',
            'color':'white'
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
], style={'overflowX': 'auto'})  # Ensure horizontal scrolling is enabled for the container

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

