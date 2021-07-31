def gen_primes():
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


def is_prime(n):
    if n in [1,2,3]:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True