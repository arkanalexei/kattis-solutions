who_cares = int(input())
while who_cares > 0:
    number = str(input())
    countr = 0
    i = -1
    while number[i] == '0':
        if number[i] == '0':
            countr += 1
            i = i - 1

    notnull = number.strip('0')
    result = int(notnull) - 1
    output = str(result)

    while countr > 0:
        output += '0'
        countr = countr - 1

    print(int(output))
    who_cares = who_cares - 1