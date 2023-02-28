n = int(input())
arr=[]
for _ in range(n):
    s= int(input())
    arr.append(s)

a = 0
b = len(arr)-1
arr.sort()
while(a<=b):
    if(a==b):
        print(arr[a],end=' ')
    else:
        print(arr[b],end=' ')
        print(arr[a], end=' ')
    a+=1
    b-=1
