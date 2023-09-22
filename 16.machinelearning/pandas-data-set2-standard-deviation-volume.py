import pandas
import numpy

df = pandas.read_csv("data2.csv")

v = df['Volume']

#Finding the standard deviation:
std = numpy.std(v)

print(std)
