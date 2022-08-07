import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    s = numpy.array(arr[-1::-1],float)
    return s
arr = input().strip().split(' ')
result = arrays(arr)
print(result)