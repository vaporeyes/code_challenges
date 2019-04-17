def is_prime(n):
    if n in [1,2,3]:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def consec_prime_sum(n):
    """
    get the sum of most consecutive primes below n
    """
    max_sum = 0
    max_run = 0
    for i in range(len(primes)):
        sums = 0
        for j in range(i, len(primes)):
            sums += primes[j]
            if sums > n:
                break
            if is_prime(sums) and sums > max_sum and j - i > max_run:
                max_run = j - i
                max_sum = sums
    return max_sum