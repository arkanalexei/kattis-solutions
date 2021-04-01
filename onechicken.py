x,y = input().split()
a = int(x)
b = int(y)

if a < b and (b-a) == 1:
    print("Dr. Chaz will have " + str(b-a) + " piece of chicken left over!")
elif a < b:
    print("Dr. Chaz will have " + str(b - a) + " pieces of chicken left over!")
elif a > b and (a-b) == 1:
    print("Dr. Chaz needs " + str(a - b) + " more piece of chicken!")
else:
    print("Dr. Chaz needs " + str(a-b) + " more pieces of chicken!")