c = int(bin(int(input()))[2:])
d = 0
while (c > 0):
    r = c % 10
    d = (d * 10) + r
    c = c // 10

e = "0b" + str(d)
print(int(e, 2))