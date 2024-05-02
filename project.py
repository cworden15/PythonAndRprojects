"""This file was written by Chris Worden for Data 375. This file contains the 
semester project for Data 375 Fall semester of 2023. This project will be focused 
on data behind fantasy football. This program is in no way accurate. First, the 
prediction model(linear regression) is not enough on its own. One major flaw 
with this is that the projection may end up being negative if the players performance 
has decreased over the season. While negative points are possible, it is very unlikely. 
I hope to improve this model in the future. However, I think this is a good first start. 
I formatted this project as more of an application rather than just an analysis, 
so running the program(at least in Rstudio) is a little more complicated. Every method 
and the playerDf must be loaded in the enviroment to run. Once everything is loaded in, 
the call to main can be called and the program will run. 
"""
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np
import requests
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Globals 
playerDf = scrape()
playerDf.drop(["AVG","TTL"],axis = 1,inplace = True)
# changing the index for easy access
playerDf.set_index('Player', inplace=True)


"""The main function. This is where all of the code will be executed."""
def main():
  playerInput = input("Please enter a player you would like to look up?")
  playerOptions = int(input("What would you like to know about this player? "
  "\nYour options are: \n1:projected points for current week "
  "\n2:visualization of player's fantasy points"
  "\n3: See stats of player"))
  takeInput(playerInput,playerOptions)
  

    
"""This function creates the data frame of the nfl players stats.
This function uses the beatiful soup library to scrape fantasy pros
to get the data. This function returns the data frame found from the first
table on fantasy pros."""  
def scrape():
  url = 'https://www.fantasypros.com/nfl/reports/leaders/'

  # Send a GET request to the website
  response = requests.get(url)

  # Parse the HTML content
  soup = BeautifulSoup(response.content, 'html.parser')

  # Find the table in the HTML
  table = soup.find('table')

  # creating the data frame 
  df = pd.read_html(str(table))[0]
  return df

"""This functions purpose is to process user input. User input will be
a players name followed by an option listed. THis function does not account
for misinputs. The program will crash is a name is mispelled."""

def takeInput(player,options):
  # stripping the players name of whitespace
  playerName = player.strip()
  # getting row of player from the data frame
  playerData = playerDf.loc[playerName]
  
  # projection option
  if options == 1:
    print(f"{playerName} is projected: {projections(playerData)}")
 
  if options == 2:
    graphThePlayersScore(playerData,playerName)
    
  if options == 3:
    getStats(playerData)
    

def projections(player): 
  # create a mask to deal with non numeric values
  mask = (player[3:14] != "BYE") & (player[3:14] != "-")
  # Correct the range for X aka weeks played
  X = np.array(range(1, 12))[mask].reshape(-1, 1)
  Y = player[3:14][mask].values.reshape(-1, 1)     
  # Perform Linear Regression
  model = LinearRegression()
  model.fit(X, Y)

  # Results
  slope = model.coef_[0][0]
  intercept = model.intercept_[0]
  score = model.score(X, Y) 
  projected = slope*14 + intercept
  return projected

def graphThePlayersScore(player,playerName):
  # Convert all values to numeric, non-numeric values become NaN
  numeric_scores = pd.to_numeric(player, errors='coerce')

  # Optional: Replace NaN values with a default value (e.g., 0)
  temp_list = numeric_scores.fillna(0)

  weeks = temp_list.index[3:14]  # Week numbers
  points = temp_list.values[3:14]  # Points per week

  plt.figure(figsize=(10, 6))
  plt.plot(weeks, points, marker='o')  
  plt.title( 'Fantasy Football Points Per Week')
  plt.xlabel('Week')
  plt.ylabel('Points')
  plt.show()
    
  else:
    print(f"No numeric data available to plot for {playerName}.")

def getStats(player):
  
  # Convert all data to numeric, assuming non-numeric data is represented by NaN
  player_data_numeric = pd.to_numeric(player, errors='coerce')
  player_data_numeric.dropna(inplace=True)
  current_weeks = player_data_numeric[3:14]
  # Calculate statistics
  mean = current_weeks.mean()
  variance = current_weeks.var()
  maximum = current_weeks.max()
  minimum = current_weeks.min()
  sum_points = current_weeks.sum()

  # Print statistics
  print(f"Statistics for {player}:")
  print(f"Mean: {mean}")
  print(f"Variance: {variance}")
  print(f"Maximum: {maximum}")
  print(f"Minimum: {minimum}")
  print(f"Total Points: {sum_points}")
  
if __name__=="__main__": 
    main() 
