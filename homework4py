numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n / 1) - 1):
        if n % i == 0:
            return False
    return True

primes = [n for n in numbers if is_prime(n)]
not_primes = [n for n in numbers if not is_prime(n)]

print("primes:", primes)
print("not_prime:", not_primes)
