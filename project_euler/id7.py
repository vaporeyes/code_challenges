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

def nth_prime(n):
	l = []
	for p in gen_primes():
		if len(l) == n + 1:
			break
		else:
			l.append(p)
	return l[n - 1]

if __name__ == "__main__":
	nth_prime(10001)