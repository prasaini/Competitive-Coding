def fourElements(arr):
    d = dict()
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            sum = arr[i]+arr[j]
            if sum in d:
                print(str(d[sum])+',('+str(arr[i])+', '+str(arr[j])+')')
                return
            else:
                d[sum]=(arr[i],arr[j])

a = [3, 4, 7, 1, 2, 9, 8]
fourElements(a)