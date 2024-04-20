# Milestone 4 Reflection

During Milestone 4, several enhancements were made to address feedback received during Milestones 3 Peer Review and Joel's Feedback. Below are the key changes:

## Layout Changes
- The Dashboard Fav icon has been added as a final touch.
- An About us page has been added with a short description of all members. A disclaimer about the dataset and its potential bias was added to ensure no misconceptions about the used dataset are made by users. Additionally, a link to the GitHub Repository was also added.
- Color Scheme Clash (Major Feedback from Joel): The color scheme being used across various visual components was slightly misleading since the colors represented different values on different charts. This was rectified by adding a note at the end of the Dashboard stating the color schemes may vary and represent different values across different components.
- Filter Selection showed Empty Visuals (Major Feedback from Joel): When a dropdown had no selection made, all the visuals on the dashboard became blank. This doesn't have a good UI feel, so to address this, a Yellow Div was added (becomes visible at the bottom of the page) that asks the user to make a selection in order to see data in the charts.
- Overall Styling: The dashboard had some issues in how the information was being represented. This was a recurring point in peer review feedback, and this has been incorporated. A Div is used for each dashboard component to keep things consistent.
- Overlapping Div Components: Some of the Divs were overlapping with the Filter/Slicers on the top of the Dash app. This has been rectified for a nicer look and feel.
- HeatMap Chart Alignment: The Heatmap was hard to read and it was not fitting the page very well, hence it was placed on the top right instead of the bottom right and the axis were rotated so it fits better and is more interpretable.
- Voting Count Fairness Explanation: The Voting Count is a metric on the dashboard which is hard to understand. A on-hover definition icon was introduced to show the definition of what that means for easier navigation of the dashboard. This was a peer review comment as well as Joel's comment.
- Clickable Legend: The Stacked Bar charts had a clickable legend that filtered only that particular chart but no cross-filtering was incorporated with other charts. Hence, for simplicity, this functionality was turned off.
- The y-axis for the 2 Stacked Bar charts on the Top-left was added back since the charts are slightly apart and it is harder to interpret the data using a common axis.
- Redundant Labels: This was a peer review comment as well, the redundant labels Race and Education Level were removed from the Stacked Bar charts.
- Performance Enhancements were made in terms of switching to parquet and introducing caching to speed things up.

## Dashboard Overall Reflection and Limitations

Overall, based on Joel's and Peer's Feedback, the dashboard displayed the information/data well and the dashboard was easy to navigate and use. However, some small issues with interpretation and usage were highlighted as explained above and these are now fixed. Some of the limitations that could be addressed are as follows:

- Limited Dataset: The dashboard's analysis and insights are limited by the dataset used. Expanding the dataset or incorporating additional data sources could provide more comprehensive insights.
- Lack of Real-time Data: The dashboard relies on static data and does not update in real-time. Incorporating real-time data updates could provide users with more up-to-date information.
- Interpretation Complexity: Some visualizations may still pose challenges in interpretation for users who are not familiar with the subject matter. Providing additional explanations or tooltips could enhance understanding.
- Cross-Filtering Functionality: While clickable legends were turned off for simplicity, enabling cross-filtering functionality between different charts could provide users with more interactive insights.

Overall, Milestone 4 represents a significant improvement in the dashboard's usability and visual appeal, addressing many of the issues raised during previous reviews. However, there are still areas for improvement to enhance the dashboard's functionality and user experience further.
