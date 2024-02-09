numbers = [1, 2, 3, 100, 13, 5, 12, 7, 8, 99, 10, 11, 15, 17]
primes = list(filter(lambda x: all(x % i != 0 for i in range(2, x)), numbers))
print("Prime numbers are:", primes)