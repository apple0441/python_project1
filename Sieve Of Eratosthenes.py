def SieveOfEratosthenes(n):
    p = 2
    primes = []
    for i in range(2, n+1):
        primes.append(i)
    while(p * p <= n):
        for i in range(p*p, n+1, p):
            if i in primes:
                primes.remove(i)
        p+=1
    return primes

if __name__ == '__main__':
    print(SieveOfEratosthenes(30))
