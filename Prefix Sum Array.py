'''Given an array arr[] of size N, find the prefix sum of the array. 
A prefix sum array is another array prefixSum[] of the same size, 
such that the value of prefixSum[i] is arr[0] + arr[1] + arr[2] . . . arr[i].'''

def prefix_sum(arr):
    n = len(arr)
    for i in range(1,n):
        arr[i]=arr[i]+arr[i-1]
    
arr = [10,20,10,5,15]
# output = [10,30,40,45,60]
prefix_sum(arr)
print(arr)
