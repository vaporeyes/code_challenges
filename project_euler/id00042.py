# coded triangle 
import string

alpha = list(set(string.ascii_uppercase))

alpha_dict = {}
for k,v in enumerate(sorted(alpha)):
    alpha_dict[v] = k

l = []
tri_num = lambda x: int(0.5 * (x * (x + 1)))
for i in range(1000):
    l.append(tri_num(i))

c = []
with open('p042_words.txt') as f:
    for name in [file for file in f.readlines()][0].split(","):
        if sum([alpha_dict[x]+1 for x in name.replace("\"",'')]) in l:
            c.append(name.replace("\"",''))

print(len(c))