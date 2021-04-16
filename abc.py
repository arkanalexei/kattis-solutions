number = input().split()
order = input()
output_number = []
stringed_number = ''

for num in number:
    output_number.append(int(num))

sorted_number = sorted(output_number)

if order == 'ABC':
    print("{} {} {}".format(sorted_number[0],sorted_number[1],sorted_number[2]))
elif order == 'ACB':
    print("{} {} {}".format(sorted_number[0], sorted_number[2], sorted_number[1]))
elif order == 'BAC':
    print("{} {} {}".format(sorted_number[1], sorted_number[0], sorted_number[2]))
elif order == 'BCA':
    print("{} {} {}".format(sorted_number[1], sorted_number[2], sorted_number[0]))
elif order == 'CAB':
    print("{} {} {}".format(sorted_number[2], sorted_number[0], sorted_number[1]))
elif order == 'CBA':
    print("{} {} {}".format(sorted_number[2], sorted_number[1], sorted_number[0]))
else:
    print("You typed the incorrect format")