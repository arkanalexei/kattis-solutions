number = str(input()).split()
new_number = []
for num in number:
    new_number.append(int(num))

r = new_number[0]
c = new_number[1]

print((r-c) * (r-c) / (r * r) * 100)