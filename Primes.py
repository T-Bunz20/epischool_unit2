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

def is_palindrome(num):
    i = 0
    j = len(str(num)) - 1
    while(i < j):
        first = str(num)[i]
        last = str(num)[j]
        if(first != last):
            return False
        i += 1
        j -= 1
    return True

def palindrome_primes(digits):
    output = []
    for i in range(10**(digits - 1), 10**digits):
        if is_prime(i):
            if is_palindrome(i):
                output.append(i)
    return output
