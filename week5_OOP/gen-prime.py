# Write a generator, genPrimes, that returns the sequence of prime \
# numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...
# Have the generator keep a list of the primes it's generated. \
# A candidate number x is prime if (x % p) != 0 for all earlier primes

def genPrimes():
    num = 1
    primes = []
    while True:
        num += 1
        isPrime = True
        for p in primes:
            if num % p == 0:
                isPrime = False
        if isPrime:
            primes.append(num)
            yield num

test = genPrimes()
print(test.__next__())
print(test.__next__())
print(test.__next__())
