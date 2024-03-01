import time
import math

def delayed_sqrt(num, delay):
    time.sleep(delay / 1000)
    return math.sqrt(num)

num = int(input())
delay = int(input())
result = delayed_sqrt(num, delay)
print(f"Square root of {num} after {delay} miliseconds is {result}")