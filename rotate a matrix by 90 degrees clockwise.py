l = [[1,2,3],[4,5,6],[7,8,9]]
m = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(l)):
    for j in range(len(l[0])):
        m[i][j]=l[j][i]

for i in range(len(l)):
    m[i]=m[i][::-1]
print(m)
