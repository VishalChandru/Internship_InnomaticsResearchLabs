import numpy
tup = tuple(map(float,input().split()))
x = int(input())
print(numpy.polyval(list(tup),x))