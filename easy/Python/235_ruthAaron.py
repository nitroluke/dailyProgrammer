def is_factor(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_factors(num):
    factors = []
    for i in range(2, num):
        if is_factor(i):
            factors.append(i)
    return factors

print(prime_factors(100))
