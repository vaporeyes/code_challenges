import turtle


def sum_spiral(x):
	"""
	set x to the size of the spiral
	"""

	turtle = turtle.TK()
	turtle.color('red')
	step = 2
	i = 1
	j = 1
	l = []
	while i <= (x*x):
		while j < 5:
			turtle.forward(j*3)
			l.append(i)
			i += step
			j += 1
		if j == 5:
			j = 1
			step += 2
			turtle.right(90)
			turtle.circle(10)
			turtle.forward(step * 3)
	done()	  
	return sum(l[:-3])

sum_spiral(10)