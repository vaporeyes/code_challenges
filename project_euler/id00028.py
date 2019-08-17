# Number spiral diagonals
def sum_spiral(x):
	"""
	set x to the size of the spiral
	"""
	step = 2
	i = 1
	j = 1
	l = []
	while i <= (x*x):
		while j < 5:
			l.append(i)
			i += step
			j += 1
		if j == 5:
			j = 1
			step += 2
	
	return sum(l[:-3])
	