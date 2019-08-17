def name_scores():
	m = []
	alphabet = {}
	for i, letter in enumerate(range(65, 91)):
		alphabet[chr(letter)] = i + 1
	with open('p022_names.txt') as f:
		names = sorted([name.replace("\"",'') for name in f.read().split(',')])
		for i, n in enumerate(names):
			m.append((i + 1) * sum([alphabet[c] for c in n]))
	
	return sum(m)