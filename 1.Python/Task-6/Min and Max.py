import numpy
n,m = map(int,input().strip().split(' '))
arr = numpy.array([input().strip().split(' ') for _ in range(n)],int)
print(numpy.max(numpy.min(arr,axis=1)))
