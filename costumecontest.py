i = 0
who_cares = int(input())
lst = []
while i != who_cares:
    lst.append(input())
    i += 1

repeat = []

for command in lst:
    if command not in repeat:
        repeat.append(command)

number = []
for costdup, costuniq in zip(lst,repeat):
    number.append(lst.count(costuniq))

minnum = min(number)
second = []

for costrep, costnum in zip(repeat, number):
    if costnum == minnum:
        second.append(costrep)
        
final = sorted(second)
for costume in final:
    print(costume)