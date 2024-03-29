**Description of the data**

The original raw data was downloaded from this URL <https://thepulseofthenation.com/#future>. This dataset is the poll result from Card Against Humanity to the nationally representative of the American public about popular social concerns during the period August 1st to 15th 2018. The survey was conducted via face-to-face, cell phone, and landlines, and respondents' demographic info and opinion choices on survey questions were collected. Though there were surveys from multiple months, due to month-by-month variation in survey questions, it is not valuable to aggregate the datasets.

The raw dataset contains 800 x 24 data points, including collected answers from 800 respondents about 8 demographical questions and 14 opinion questions. It contains 11% of missing data points mainly from redundant 'other' columns.

To better understand the public opinion of different demographic groups, we have done some initial data preprocessing and data engineering to prepare for visualization. For data preprocessing, we dropped 5 irrelevant, or vacant columns. We renamed the column title into brief phrase form.

For data engineering, we added the 'political_spectrum_score' column based on the numerical conversion of the 'ideology' choice to help understand political standing. Also, we added the 'likelihood_of_war" by adding up the number of 'yes' in the two 'war prediction' related questions so it becomes a numerical scale from 0 to 2. Further, we added the 'time_answered' column to reflect this survey period for dashboard sustainability purposes if there are more incoming surveys in future months.

The cleaned dataset contains 800 rows and 22 columns. It is structured with a focus on public opinions and demographic data, tailored to understand societal trends and political leanings. Key characteristics of this dataset include:

1.  **Demographic Information:** Columns including gender, age range, race, higher_education, and monetary_anxity provide insights into the diverse backgrounds of respondents.

2.  **Political Orientation:** Through variables like 'political_party', 'ideology', and 'political_spectrum_score', the dataset offers a detailed look into the political affiliations and opinions of individuals.

3.  **Views on Political Issues:** Responses to questions about Trump's presidency, and fairness of voting paint a picture of public sentiment on key political discussion points.

4.  **Prediction on Hot Social Topics:** Response to questions including woman_president, universal_healthcare, human_survival, america_survival, trump_2020, trump_nuclear, america_vs_russia, america_vs_china, and likelihood_of_war provides a holistic view of general perspectives on prediction of hot social topics.

5.  **Data Collection Period:** The last column of the dataset reflects the survey collected year and month. It serves the purpose of keeping the dashboard sustainable and supporting cross-period comparisons.

This dataset plays a vital role in enhancing the public's insight into the political and social views of Americans. Our goal is to investigate the connections between demographic attributes and societal and political opinions among the American populace. The objective is to develop a user-friendly dashboard tool that provides valuable insights to assist in policymaking, political campaigns, news coverage, investment strategies, and more. This initiative aims to grasp the prevailing sentiment of the nation as of August 2018.
