# sum square difference

def sum_squares_diff(n):
    sum_squares = sum([i * i for i in range(1, n + 1)])
    square_sum = sum([i for i in range(1, n + 1)]) * sum([i for i in range(1, n + 1)])
    return square_sum - sum_squares

