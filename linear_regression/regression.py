'''
	Program to predict life expectancy from body mass index(BMI)
	Using supervised learning approach to train the model
	Using Supervised Linear Regression to train the model

'''

import pandas as pd
from sklearn import linear_model

# read data 
bmi_life_data = pd.read_csv('bmi_and_life_expectancy.csv')

x_values = bmi_life_data[['BMI']]
y_values = bmi_life_data[['Life expectancy']]

# Fit the model to the data
bmi_life_model = linear_model.LinearRegression()
bmi_life_model.fit(x_values, y_values)

# Predict the life expectancy using the BMI of 21.07931
laos_life_exp = bmi_life_model.predict(21.07931)

print laos_life_exp