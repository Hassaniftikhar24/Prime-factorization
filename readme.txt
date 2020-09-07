# Input: An integer value
# Output: Returns the prime factors of that number
# Method: By using a user defined function

Logic: 

List used for storing prime factors
Append function used to update the prime factors and make an array
Divisor is starting from 2 i.e. the first prime number

Executable Code: 

a = input("Enter your number: ")
a = int (a)
def get_prime_factors(N):
    factors = list()
    divisor = 2
    while divisor <= N:
        if (N % divisor) == 0:
            factors.append(divisor)
            N = N / divisor
        else:
            divisor += 1
    return factors

x = get_prime_factors(a)
print(x)

Another approach: (Problem with having the repeated prime factor not appearing in the output)

import numpy as np
b = input("Enter a number : ")
b = int(b)


def get_prime_factors(a):
    ar = []
    if a > 1:
        for i in range(2, a + 1):
            n = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    n += 1
            if n == 2:
                ar.append(i)
    x = len(ar)
    ar = np.array(ar)
    #print(x)
    list_prime_numbers = []
    for k in range(0, x):
        if a % ar[k] == 0:
            list_prime_numbers.append(ar[k])
    print(list_prime_numbers)
    return list_prime_numbers


get_prime_factors(b)


