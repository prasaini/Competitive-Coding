def rearrange(arr):
    n = len(arr)
    for i in range(1,n-1):
        if(arr[i]==(arr[i-1]+arr[i+1])//2):
            arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr

if __name__ == "__main__" :
    arr = [ 6, 9, 12, 25, 50, 75 ];
    a = rearrange(arr)
    print(arr)