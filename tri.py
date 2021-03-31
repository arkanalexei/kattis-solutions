number = str(input())
number_split = number.split()
append_num = []

for num in number_split:
    append_num.append(int(num))

if append_num[0] + append_num[1] == append_num[2]:
    print(str(append_num[0]) + "+" + str(append_num[1]) + "=" + str(append_num[2]))
elif append_num[0] - append_num[1] == append_num[2]:
    print(str(append_num[0]) + "-" + str(append_num[1]) + "=" + str(append_num[2]))
elif append_num[0] / append_num[1] == append_num[2]:
    print(str(append_num[0]) + "/" + str(append_num[1]) + "=" + str(append_num[2]))
elif append_num[0] * append_num[1] == append_num[2]:
    print(str(append_num[0]) + "*" + str(append_num[1]) + "=" + str(append_num[2]))
elif append_num[1] + append_num[2] == append_num[0]:
    print(str(append_num[0]) + "=" + str(append_num[1]) + "+" + str(append_num[2]))
elif append_num[1] - append_num[2] == append_num[0]:
    print(str(append_num[0]) + "=" + str(append_num[1]) + "-" + str(append_num[2]))
elif append_num[1] / append_num[2] == append_num[0]:
    print(str(append_num[0]) + "=" + str(append_num[1]) + "/" + str(append_num[2]))
elif append_num[1] * append_num[2] == append_num[0]:
    print(str(append_num[0]) + "=" + str(append_num[1]) + "*" + str(append_num[2]))