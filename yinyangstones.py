stone = str(input())
wcountr = 0
bcountr = 0

for char in stone:
    if char == 'W':
        wcountr += 1
    else:
        bcountr += 1

if wcountr == bcountr:
    print(1)
else:
    print(0)