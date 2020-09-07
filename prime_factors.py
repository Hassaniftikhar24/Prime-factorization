# Input: An integer value
# Output: Gives all the prime factors of that number
# Method: By using a user defined function

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

