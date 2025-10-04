# compute primes upto limit

def primes(limit):
    primes = []
    for i in range(2, limit+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True