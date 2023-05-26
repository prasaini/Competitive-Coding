def findpair(arr, x):
    d = {}
    for i in range(len(arr)):
        n = x-arr[i]
        if n in d:
            return True
        d[arr[i]] = i
    return False

a = [1,2,3,-2,4]
print(findpair(a, 0))