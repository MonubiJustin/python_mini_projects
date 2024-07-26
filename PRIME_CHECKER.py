from math import ceil


def prime_checker(n):  # 5
    is_prime = True
    if n == 1:
        is_prime = False
    for i in range(2, ceil(n)+1):  # 2, 3, 4
        if n % i == 0:
            is_prime = False
    if is_prime:
        print('This is a prime number')
    else:
        print('This is not a prime number')


n = int(input('Enter a number:\n'))
prime_checker(n)
