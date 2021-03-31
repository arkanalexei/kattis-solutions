import sys
# Taking input
def multi_input():
    dom = 0
    while dom != 10:
        data = input()
        if not data: break
        yield data
        dom += 1

userInput = list(multi_input())

# Converting to list of integers
numbers = [int(i) for i in userInput]

# Code
distinct_mod = []
for num in numbers:
    distinct_mod.append(num % 42)

output = set()
for x in distinct_mod:
    output.add(x)
print(len(output))