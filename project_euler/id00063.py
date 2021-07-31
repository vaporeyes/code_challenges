len([(i, x, i**x) for i in list(range(1,101)) for x in list(range(1,101)) if len(str(i**x)) == x])
