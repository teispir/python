import pandas
import numpy

df = pandas.read_csv("data2.csv")

v = df['Weight']

# Finding the mean value of data2.csv dataset:
mean = numpy.mean(v)

print(mean)

