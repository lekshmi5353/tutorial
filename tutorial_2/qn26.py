def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

numbers = list(map(int, input("Enter a list of positive integers: ").split()))
primes = [num for num in numbers if is_prime(num)]
composites = [num for num in numbers if not is_prime(num) and num > 1]
print("Prime numbers:", primes)
print("Composite numbers:", composites)
