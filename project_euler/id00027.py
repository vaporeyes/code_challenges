i_max, j_max, n_max = 0,0,0
for i in range(-999,1001,2):
    for j in range(-999,1001,2):
        n = 0
        while is_prime(abs(n * n + i * n + j)):
            n += 1
            if n > n_max:
                i_max = i
                j_max = j
                n_max = n