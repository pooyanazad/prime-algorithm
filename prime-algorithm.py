#just another way to find prime numbers, If list empty its prime
def is_prime(num):
    """Return True if `num` is prime, otherwise False."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
