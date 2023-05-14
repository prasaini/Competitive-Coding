def remove_duplicate(arr):
    n = len(arr)
    x = 1
    for i in range(1,n):
        if arr[i-1]!=arr[i]:
            arr[x]=arr[i]
            x+=1
    return x

arr = [1,1,2,2,2,3,3,4,5,6,7,8]
a = remove_duplicate(arr)
for i in range(a):
    print(arr[i])