listNumbers = input().split()
intListNumbers = []
for i in listNumbers:
    intListNumbers.append(int(i))
def filter_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return [n for n in numbers if is_prime(n)]
print(filter_prime(intListNumbers))