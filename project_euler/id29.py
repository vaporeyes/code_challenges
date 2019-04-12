# distinct powers
def get_distinct_powers(n):
	"""
	iterative way
	"""
	l = []
	for a in range(2, n + 1):
		for b in range(2, n + 1):
			l.append(a**b)
	
	return len(set(l))

def get_powers(start,end):
	"""
	list comprehension way
	"""
	return [a**b for a in range(start, end) for b in [b for b in range(start, end)]]