def calc_fib_num(n):
    if n == 0:
        # Base case 0.
        return 0
    elif n == 1:
        # Base case 1.
        return 1
    else:
        return calc_fib_num(n - 1) + calc_fib_num(n - 2)
