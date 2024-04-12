from dash import Dash, html, dcc, Input, Output
from components import create_donut_chart, create_stacked_chart_race, create_stacked_chart_education, create_war_likelihood_chart, table_component
from data import df



def update_donut_chart(age_range,
                       education,
                       ideology,
                       race):
    filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]
    filtered_df = filtered_df[filtered_df['higher_education'].isin(education)]
    filtered_df = filtered_df[filtered_df['ideology'].isin(ideology)]
    filtered_df = filtered_df[filtered_df['race'].isin(race)]

    return create_donut_chart(filtered_df)



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
    return data