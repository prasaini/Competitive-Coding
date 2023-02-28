z = int(input())
for _ in range(z):
    n,x = map(int,input().split(' '))
    count =0
    l=list(map(int,input().split(' ')))
    even=0
    for a in l:
        if a%2==0:
            even += 1
    if even == n and x%2==0:
        print('-1')
    elif even == 0:
        print('0')
    elif x%2 == 0:
        print(even)
    else:
        print((even+1)//2)
