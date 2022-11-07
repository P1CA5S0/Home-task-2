import random

a = random.randint(2, 99)
b = random.randint(2, 99)
SUM = a + b
PROD = a * b
print("Sum = %s, prod = %s" % (SUM, PROD))

sum_array = []
prod_array = []
for i in range(1, 100):  # Finding numbers that are equal to the product and sum of numbers a and b
    for j in range(1, 100):
        numbers = [[i, j]]
        if i + j == SUM:
            sum_array += numbers
        if i * j == PROD:
            prod_array += numbers

answer = []
for i in range(len(sum_array)):  # Search the same elements
    for j in range(len(prod_array)):
        if sum_array[i] == prod_array[j]:
            answer.append(sum_array[i])

print("Answer: ", answer[0])
