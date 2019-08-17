def coin_sums(n, coins):
	i = 0
	ways = [0] * (n + 1)
	ways[0] = 1
	for i in range(len(coins)):
		j = coins[i]
		while j <= n:
			ways[j] += ways[j - coins[i]]
			j += 1
		i += 1
	
	return ways[-1]