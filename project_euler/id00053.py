# factorial code needed
Crn = lambda r, n: factorial(n) / (factorial(r) * factorial(n -r))
l = []
for n in range(1,101):
    for r in range(1,101):
        if r < n:
            x = Crn(r,n)
            if x > 1000000:
                l.append(x)

print(len(l))