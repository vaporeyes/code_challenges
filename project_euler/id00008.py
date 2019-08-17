with open('id8_input') as f:
    c = 0
    n = ''.join([n.strip() for n in f.readlines()])
    for i in range(len(list(n))):
        m = [int(j) for j in n[i:i+13]]
        if len(m) == 13:
            l = reduce(lambda x, y: x * y, m)
            if l > c:
                c = l
    
    print(c)