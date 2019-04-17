# Number spiral diagonals
def pcnt_prime_spiral():
	"""
	set x to the size of the spiral
	"""
	step = 2
	i = 1
	j = 1
	l = []
	primes = []
	not_primes = []
	for x in itertools.count(1):
		while i <= (x*x):
			while j < 5:
				l.append(i)
				i += step
				j += 1
				if is_prime(i):
					primes.append(i)
				else:
					not_primes.append(i)
			if j == 5:
				side_length = (i - l[-1]) + 1
				j = 1
				step += 2
				pcnt_prime = len(primes) / (len(primes) + \
					len(not_primes) + 1) * 100
		if pcnt_prime < 10:
			return side_length, pcnt_prime
			break
