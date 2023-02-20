l = [[1,2,3],[3,1,2],[2,3,1]]
n = len(l)
m = len(l[0])
s=''
for i in range(m):
    s+=str(l[0][i])
s = s+s
s1=''
flag = 0
for i in range(1,n):
    s1 = ''
    for j in range(m):
        s1+=str(l[i][j])
    if s1 in s:
        flag = 1
    else:
        flag = 0
        break
if flag == 1:
    print("yes")
else:
    print("no")
