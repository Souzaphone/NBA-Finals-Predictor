# NBA-Finals-Predictor

## Data Science Project Examining NBA Advanced Statistics
This project contains 2 files.
1. **NBA_seasons**: NBA advanced stats dating back to 2015.
2. **nba_finals.ipynb**: cleaning, visualizing, and making predictions from the data.

# NBA_seasons
Contains a CSV file for every season that I cataloged from basketball-reference.com. Contains 279 entries and 32 total features. 

# nba_finals.ipynb
The notebook is where the bulk of the coding is for the project. This is where I complete data cleaning, visualization, and championship prediction. There are plenty of comments and notes where I explain my thought process and observations.

1. Cleaning - I dropped duplicate or unnecessary features.

2. Visualizing - I used Seaborn to visualize the data. I looked for discrepancies in the data to influence my choices of features, such as if the feature leaned to one side or the other for champions or not. 

3. Prediction - I used two models to try and predict the 2024 NBA Champion: a Logistic Regression and a Random Forest Model. Both performed pretty well and had high accuracy.
