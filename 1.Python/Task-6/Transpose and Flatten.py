import numpy
n,m = map(int,input().strip().split(' '))
lis = []
n = numpy.array([input().strip().split() for _ in range(n)], int)
print(numpy.transpose(n))
print(n.flatten())