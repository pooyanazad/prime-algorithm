#just another way to find prime numbers, If list empty its prime
def is_prime(num):
    if num < 2:
        return False
    divisors = []
    for i in range(2, ((num**0.5)+1)):
        if num % i == 0:
            divisors.append(i)
    return len(divisors) == 0
n = int(input("Enter your number: "))
if is_prime(n):
    print("Its Prime")
else:
    print("Not Prime")
