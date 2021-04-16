mydict = {
    '000': 0,
    '001': 1,
    '010': 2,
    '011': 3,
    '100': 4,
    '101': 5,
    '110': 6,
    '111': 7,
}

number = str(input())
number2 = ''
number3 = ''

lst = []
lst2 = []
lst3 = []

if len(number) % 3 == 0:
    for num in number:
        lst.append(num)
else:
    number2 = '0' + number
if len(number2) % 3 == 0:
    for num in number2:
        lst2.append(num)
else:
    number3 = '0' + number2
if len(number3) % 3 == 0:
    for num in number3:
        lst3.append(num)

if len(lst) != 0:
    l = lst
elif len(lst2) != 0:
    l = lst2
elif len(lst3) != 0:
    l = lst3

n = 3
ab = [ l[i:i+n] for i in range(0, len(l), n) ]

koko = ''

for number in ab:
    for num in number:
        koko += str(num)

countr = 0
k = 0
t = 3
final = ''
while countr != len(koko) / 3:
    final += str(mydict.get(koko[k:t]))
    countr += 1
    k += 3
    t += 3

print(final)
