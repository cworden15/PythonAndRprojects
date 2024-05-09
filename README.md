This respo contains a few files in R and python that are more data science focused. I created these files during my time at university and after. As time goes on, I will be adding more. 

Project.R - 
  This is a R program that takes two csv files from kaggle(I do not have the orginal link to the data sets, so the code will be unrunnable). The csv files contain information on global emisssions of countries and gdp. The code then proceeds to us the lm function in R to
  see if a correlation exists between the two. I do not have the output file from this anymore, but I do remember the correlation was >.5, this result does not provide much insight into the relation. It doesn't imply causality or anything of the sort. The data was also visualized. 

Project.py - 
  This is a python project based on fantasy football. I used beautiful soup to get fantasy data from the 2023-2024 NFL season. I found this data from 'https://www.fantasypros.com/nfl/reports/leaders/'. I used pandas and sklearn to provide some insight into this data. 
  The projections made from this project are not accurate in any way. Linear regression was used to project fantasy football points. However, the only data that was used was from the same season. This creates a few problems. One, the training data is extremely small. 
  Two, simple linear regression was used. There are too many factors that go into a football performance, so using one variable will fall extremely short. I plan on updating this model (increase size of training data, employ different ml methods) near football season. 

someDataCleaning - 
  This is a file that I recently did (5/24) to practice data cleaning. The data was quite clean, so I did not do much to the csv file. I removed a few unwanted characters and such. 
