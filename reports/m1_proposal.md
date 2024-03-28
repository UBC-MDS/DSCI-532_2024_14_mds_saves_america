**Description of the data**

The original raw data is downloaded from this URL <https://thepulseofthenation.com/#future>. This dataset is the pull result from Card Against Humanity to the nationally representative of American public about popular social concerns during time period August 1st to 15th 2018. The survey was conducted via face to face, cell phone, and land lines, and respondents' demographic info and opinion choices on survey questions were collected.

The raw dataset contains 800 x 24 datapoints, including collected answers from 800 respondents about 7 demographical questions and 14 opinion questions. It contains 11% of missing data points mainly from redundant 'other' columns.

In order to better understand public opinion of different demographic groups, we have done some initial data preprocessing and data engineering to get prepared for visualization. For data preprocessing, we dropped 5 irrelevant, or vacant columns. We renamed column title into brief phrase form. We added the 'political_spectrum_score' column based on numerical conversion of the 'ideaology' choice to help understand political spectrum. Further, we added the 'time_answered' column to reflect this survey period for dashboard sustainability purpose if there are more incoming surveies in future month.

The cleaned dataset contains 800 rows and 21 columns. It is structured with a focus on public opinions and demographic data, tailored to understand societal trends and political leanings. Key characteristics of this dataset include:

1.  **Demographic Information:** Columns including gender, age range, race, higher_education, and monetary_anxity provide insights into the diverse backgrounds of respondents.

2.  **Political Orientation:** Through variables like 'political_party', 'ideology', and 'political_spectrum_score', the dataset offers a detailed look into the political affiliations and opinions of individuals.

3.  **Views on Political Issues:** Responses to questions about Trump's presidency, and fairness of voting paint a picture of public sentiment on key political discussion points.

4.  **Prediction on Hot Social Topics:** Response to questions including woman_president, universal_healthcare, human_survival, america_survival, trump_2020, trump_nuclear, america vs russia, america vs china provides holistic view of general perspectives on prediction of hot social topics.

5.  **Data Collection Period:** The last column of the dataset reflects the survey collected year, month. It serves the purpose to keep the dashboard sustainable and support cross period comparisons.

This dataset will be instrumental in supporting the public and professionals in understanding Americans' political standings and social opinions. It will facilitate the exploration of correlations across demographic characteristics against sociological and political opinions. The aim is to derive a useful, straightforward, and easily accessible dashboard tool. This tool will leverage insights to faciliate policy-making, political campaigning, news reporting, investment decisions, etc. and understand the pulse of the nation as of August 2018.
