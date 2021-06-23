def big_fibonacci(digits):
    prev_fib_num = 1
    fib_num = 1
    while(len(str(fib_num)) != digits):
        temp = fib_num
        fib_num = fib_num + prev_fib_num
        prev_fib_num = temp
    return fib_num