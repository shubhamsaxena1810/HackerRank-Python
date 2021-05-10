import numpy

def arrays(arr):
    # complete this function
    arr=numpy.array(arr,float)
    arr=arr[::-1]
    return arr
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)