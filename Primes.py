def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if(num % i == 0):
            return False
    return True

def primes_below(num):
    output = []
    for i in range(2,num):
        if is_prime(i):
            output.append(i)
    return output
