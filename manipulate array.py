n = int(input())
for _ in range(n):
    a = int(input())
    l=list(map(int,input().split(' ')))
    l.sort()
    start=0
    end = a-1
    while(start<=end):
        if(start==end):
            print(l[start])
        else:
            print(l[start])
            print(l[end])
        start+=1
        end -=1