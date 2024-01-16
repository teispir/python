import pandas
from sklearn import linear_model

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedCO2 = regr.predict([[3300, 1300]]) # weight increased by 1 kg (from 2300) and Volume 1.3

print(predictedCO2) # it prints 114.75968007

# We have predicted that a car with 1.3 liter engine, and a weight of 3300 kg, will release approximately 115 grams of CO2 for every kilometer it drives.

# 107.2087328 + (1000 * 0.00755095) = 114.75968

# 107.2087328 was printed by pandas-linear-regression.py

