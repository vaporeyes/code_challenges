def digital_root(n):
    if len(str(n)) == 1:
        return n
    return digital_root(sum([int(i) for i in list(str(n))]))
    
def factorial(n):
    """
    factorial of a number, recursive
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def factors(x):
    """
    return all factors of a number minus 1 and itself
    """
    result = []
    i = 1
    while i*i <= x:
        if x % i == 0:
            result.append(i)
            if x/i != i:
                result.append(x/i)
        i += 1
    return [int(x) for x in sorted(list(set(result)))[1:-1]]

def is_prime(n):
    """
    returns true if number is prime
    """
    if n in [1,2,3]:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def gen_primes(t='gen',i=None):
    """
    gen => generate unlimited primes
    nth => generate up to the nth prime
    up2 => generate primes to up value
    """
    if t in ['nth','up2','gen']:
        if t == 'nth':
            D = {}
            q = 2
            while len(D) < i:
                if q not in D:
                    yield q
                    D[q * q] = [q]
                else:
                    for p in D[q]:
                        D.setdefault(p + q, []).append(p)
                    del D[q]
                q += 1            
        elif t == 'up2':
            D = {}
            q = 2
            while q < i:
                if q not in D:
                    yield q
                    D[q * q] = [q]
                else:
                    for p in D[q]:
                        D.setdefault(p + q, []).append(p)
                    del D[q]
                q += 1
        elif t == 'gen':
            D = {}
            q = 2
            while True:
                if q not in D:
                    yield q
                    D[q * q] = [q]
                else:
                    for p in D[q]:
                        D.setdefault(p + q, []).append(p)
                    del D[q]
                q += 1
        else:
            print("type required: nth, up2, gen")
