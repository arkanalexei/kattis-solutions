n = int(input())
def multi_input():
    dom = 0
    while dom != 1:
        data = input().split()
        if not data: break
        yield data
        dom += 1

userInput = list(multi_input())

string_number = []
for char in userInput:
    for num in char:
        if num != ' ':
            string_number.append(num)


new_numbers = []
for char in string_number:
    new_numbers.append(int(char))
    
# CODE

negative_numbers = []
for num in new_numbers:
    if num < 0:
        negative_numbers.append(num)

total_negative_number = 0

for num in negative_numbers:
    total_negative_number += num

print(abs(total_negative_number))