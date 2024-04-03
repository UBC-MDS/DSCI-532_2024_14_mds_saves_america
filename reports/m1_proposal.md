## **1. Motivation and Purpose**

Our role: Data Scientists and Election Polling Analysts

Target audience: Undecided American Voters

With 2024 USA elections coming up, Americans find themselves with a difficult decision on who to elect as their new Commander-in-chief, Joseph Robinette Biden, also known as Joe Biden, representing the Democratic Party, or Donald John Trump, also known as Donald Trump representing the Republican Party. This is a challenging decision to make as an American citizen, seeing as both candidates have held office, and both have had their respective controversies before. Given these factors, addressing the issue on who better suits an American citizen's ideology is crucial for The People to make this important decision.

Our dashboard will act as a tailored electorar guide for the upcoming 2024 USA elections, using the dataset The Pulse of the Nation from August 2018. It provides potential voters with an intuitive interface to explore candidate ideologies, ethnical demographics, and public opinion. With interactive features, voters can make better informed decisions aligned with their values.

## **2. Description of the Data**

The original raw data was downloaded from this URL <https://thepulseofthenation.com/#future>. This dataset contains the poll results from Cards Against Humanity regarding popular social concerns among a nationally representative sample of the American public during the period from August 1st to August 15th, 2018. The survey was conducted through face-to-face interviews, cell phone calls, and landline calls, collecting respondents' demographic information and their opinions on survey questions. Although surveys were conducted over multiple months, due to variations in survey questions month by month, it was not feasible to aggregate the datasets.

The raw dataset contains 800 rows and 24 columns, including responses from 800 respondents to 8 demographic questions and 14 opinion questions. It contains 11% missing data points, primarily from redundant 'other' columns.

To better understand public opinion across different demographic groups, we conducted some initial data preprocessing and data engineering to prepare for visualization. In the preprocessing phase, we removed 4 irrelevant or vacant columns and renamed the remaining columns to more intuitive names.

In the data engineering phase, we added the 'political_spectrum_score' column, encoding categorical values for 'ideology' to aid in understanding political leanings. Additionally, we calculated the 'likelihood_of_war' by summing up the number of 'yes' responses in the two columns related to war likelihood, creating a numerical scale between 0 and 2. Furthermore, we included the 'time_answered' column to reflect the survey period for sustainability purposes of the dashboard, in case more surveys are conducted in future months.

The cleaned dataset now comprises 800 rows and 23 columns. It is structured to focus on public opinions and demographic data, tailored to understand societal trends and political leanings. Key characteristics of this dataset include:

1.  **Demographic Information:** Columns including gender, age, age range, race, higher_education, and monetary_anxiety provide insights into the diverse backgrounds of respondents.

2.  **Political Orientation:** Variables like 'political_party', 'ideology', and 'political_spectrum_score' offer a detailed look into the political affiliations and opinions of individuals.

3.  **Views on Political Issues:** Responses to questions about Trump's presidency and the fairness of voting paint a picture of public sentiment on key political discussion points.

4.  **Prediction on Hot Social Topics:** Responses to questions including woman_president, universal_healthcare, human_survival, america_survival, trump_2020, trump_nuclear, america_vs_russia, america_vs_china, and likelihood_of_war provide a holistic view of general perspectives on hot social topics.

5.  **Data Collection Period:** The last column of the dataset reflects the year and month when the survey was conducted. It serves the purpose of keeping the dashboard sustainable and supporting cross-period comparisons.

This dataset plays a vital role in enhancing the public's insight into the political and social views of Americans. Our goal is to investigate the connections between demographic attributes and societal and political opinions among the American populace. This initiative aims to grasp the prevailing sentiment of the nation as of August 2018.

## **3. Research Question**

Our dashboard aims to help undecided American voters for the upcoming elections on who will better represent them in the upcoming elections for Commander-in-cheif.

1.  Lorenzo, a 45 year old store owner in Florida, is involved in his local community and values staying informed about political matters. Lorenzo is interested in knowing more about the upcoming 2024 USA elections, and seeks to use the electoral guide dashboard to gain valuable insights into the ideologies of the presidential candidate, especially the Republican Party candidate. As a business owner, Lorenzo understands the importance of political decisions on his business and the community. His main goal is to learn as much as possible from the Republican Party candidate, as this is his first choice, as he has historically been a Republican.

2.  Stefano, a 49 year old employee at an oil and gas company in California, nearing retirement, is highly interested on the candidates' views on oil and gas. Stefano values the insights found on the dashboard because, as he is nearing retirement, he wants to know how these elections will affect his 401k and his current job as an employee in a controversial field. Stefano seeks to learn more about the Republican Party candidate, as he has been a Democrat for a better part of his adult life, but has felt the current government has not backed him up in retirement and oil and gas matters.

3.  Donald, a 77 year old businessman residing in New York, brings decades of experience in the business field. He has been an entrepreneur for several companies, so he is very keen on learning how these future elections will affect his businesses. Donald has been a Republican most of his life, and is very interested on the Republican Party candidate because he feels like his views align very well with this candidate. Donald feels like this dashboard will help him clear up his doubts about the party, seeing as the country has been divided on political parties, and misinformation seems rampant on social media in the past couple of years.

## **4. App Sketch and Dashboard Description**

The main page of the app presents a summary of the survey data, providing general statistics and comparisons related to American elections. The main page is divided into two sections: general correlations regarding political affiliations and opinions on American survival, and the elections section, which covers public opinion on Donald Trump.

In the general correlations section: - Stacked bar charts illustrate the breakdown of Americans' political affiliations by demographics such as race and education level. - A bar chart displays the likelihood of war as perceived by Americans, compared with their beliefs about America's survival over a century.

The elections section focuses on perceptions surrounding Donald Trump: - A donut chart depict the likelihood of Trump's re-election in relation to individuals' concerns about their monetary situation. - A frequency table examines approval of Trump and beliefs about the fairness of vote counting during elections.

All comparative statistical distributions can be filtered via the top filtering pane, allowing users to filter by age range, education level, political ideology, and race using dropdown menus and sliders. The color scheme chosen for the app is inspired by the American flag, using different colors to distinguish between groups in chart breakdowns.
