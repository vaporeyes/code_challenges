def fifth_powers(n):
	"""
	find the sum of powers to n
	"""
	i = 1
	l = []
	max_val = (9**n) + (9**n) + (9**n) + (9**n)
	print("max_val: {0}".format(max_val))
	while i < max_val:
		val = (sum([(int(x)**n) for x in list(str(i))]))
		if val == i and val != 1:
			l.append(val)
		i += 1
	
	return sum(l)
	