import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

# What is the age that 90% of the people are younger than? this number is given by function percentile

x = numpy.percentile(ages, 90)

print(x)