'''Given an array arr[] of size N. Given Q queries and in each query 
given L and R, Print the sum of array elements from index L to R.'''

def prefix_sum(arr):
    new=[0]*len(arr)
    new[0]=arr[0]
    for i in range(1,len(arr)):
        new[i]=new[i-1]+arr[i]
    print(new)
    return new

def sum_in_range(arr,Range):
    arr = prefix_sum(arr)
    # arr = [3, 9, 11, 19, 28, 30]
    arr = [0]+arr+[0]
    # arr = [0, 3, 9, 11, 19, 28, 30, 0]
    n = len(Range)
    l=[]
    for i in range(n):
        left = Range[i][0]
        right = Range[i][1]
        l.append(arr[right]-arr[left-1])
    print(l)


arr = [3, 6, 2, 8, 9, 2]
Range = [[2, 3], [4, 6], [1, 5], [3, 6]]
sum_in_range(arr,Range)