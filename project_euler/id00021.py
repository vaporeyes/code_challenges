import math


def divisors(n):
	divs = [1]
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0 and n != i:
			divs.extend([i, n // i])
	return sum(list(set(divs)))

def sum_amicable(n):
	i = 0
	l = {}
	m = []
	while i < n:
		i += 1
		d = divisors(i)
		l[i] = d
	for j,k in l.items():
		try:
			if l[k] == j and l[j] != j:
				m.append(j)
		except KeyError:
			continue
	return sum(m)