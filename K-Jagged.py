def getPrimes(n):
    Prime = [True] * (n + 1)
    i = 2
    while (i * i <= n):
        if (Prime[i] == True):
            j = i * 2
            while (j <= n):
                Prime[j] = False
                j += i        
        i += 1
    prime = []
    for i in range(2, n + 1):
        if (Prime[i]):
            prime.append(i)   
    return prime

def isRough(n, k):
    primes = getPrimes(n)
    min_pf = n
    l=[]
    for i in range(len(primes)):
        if (n % primes[i] == 0):
            min_pf = primes[i]
            l.append(min_pf)
    a = l[0]
    return (a >= k)
n = 75
k = 3
if (isRough(n, k)):
    print(n, "is a", k,"-rough number");
else:
    print(n, "is not a", k, "-rough number");