import sys
n = int(input())
def multi_input():
    dom = 0
    while dom != n:
        data = input()
        if not data: break
        yield data
        dom += 1

userInput = list(multi_input())
numbers = [int(i) for i in userInput]

for num in numbers:
    if num % 2 == 0:
        print(str(num) + " is even")
    else:
        print(str(num) + " is odd")

