def move_to_end(arr):
    x=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[x]=arr[i]
            x+=1
    while x<len(arr):
        arr[x]=0
        x+=1

arr=[0,0,1,2,0,3,4,0]
move_to_end(arr)
print(arr)