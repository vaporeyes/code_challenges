def divisors(n):
	divs = [1]
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0 and n != i:
			divs.extend([i, n // i])
	return list(set(divs))

def pandigital_products():
	l = []
	for i in range(9999):
		nums = [x for x in divisors(i)]
		for j in range(len(nums)):
			for k in range(1, len(nums)):
				str_num = sorted(list(str(nums[j]) + str(nums[k]) + str(i)))
				if (nums[j] * nums[k]) == i:
					if ''.join(str_num) == str(123456789):
						l.append(i)
	
	print(sum(set(l)))