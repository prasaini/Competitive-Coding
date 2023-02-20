l = [1,2,3,4,5,6,7,8,9,0]
r = int(input())
for i in range(r):
    a = l[len(l)-1]
    for j in range(len(l)-1,-1,-1):               
        l[j]=l[j-1]
    print(l)
    l[0]=a
print(l)
