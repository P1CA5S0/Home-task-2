from random import random

hits = 0
for i in range(10000):  # The number in range mean number of points
    x = random()  # Generation of random numbers
    y = random()  # Generation of random numbers
    if x * x + y * y <= 1:
        hits += 1
print(4 * hits / 10000)
