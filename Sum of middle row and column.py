a = [[1,2,3],[4,5,6],[7,8,9]]
n = len(a)
m = len(a[0])
sum = 0
sum1 = 0
for i in range(n):
    sum+=a[i][m//2]
for i in range(m):
    sum1+=a[n//2][i] 

print(sum)
print(sum1) 

