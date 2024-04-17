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

# Reflection
I believe that a large part of the success of this model stems from the great features that are collected in advanced stats at Basketball-reference.com. They are a great mix of offensive ability and defensive ability, and they are normalized well so that the data won't skew in favor of any particular feature. I originally attempted to get all data for this project using an NBA-API, but after realizing that the API only had data up until 2021 I switched to scraping data from Basketball-reference. At first, I was using Beautiful Soup to scrape the data automatically and I had this working perfectly, but then I realized that Basketball-reference has very strict request limits and I could only make 10 requests every hour or something along those lines. Instead of adding time.sleep(100) I just decided to get the data by hand as Basketball-reference has very useful table-to-CSV conversions made into the website. 

# Possible Issues
With attempting to predict the NBA champion, there is one glaring issue: there is only one champion a year. Due to this fact, there is not a lot of cases to look at that we can draw data from. As time goes on there will be more data to look at, but the reason that I only decided to look back to 2015 was the fact that the way the game is played changes rapidly, and a lot of these advanced stats become irrelevant with that change. Another issue is the way in which I measured the models. Because there is not a lot of data to look at, my accuracy values will tend to be very close as there are only so many years that my model could incorrectly select a champion. 

# Improvements
- Utilize a live-stats NBA API in order to calculate the percentages of the champion in real-time.
- Add user-crafted features based on facts that the model might not understand; made-playoffs, playoff seed, injuries, distance to travel for series, etc.
- Find a way to incorporate BS4 into this, possibly to scrape game odds from betting websites as a feature. 
