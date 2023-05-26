def subset(arr1, arr2):
    a = len(arr1)
    b = len(arr2)
    s = set()
    for i in range(a):
        s.add(arr1[i])
    c = len(s)
    for i in range(b):
        s.add(arr2[i])
    if(c==len(s)):
        return True
    else:
        return False

a = [1,2,3,4,5]
b = [2,4,5]
print(subset(a,b))