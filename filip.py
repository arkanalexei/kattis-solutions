a = input()
num1 = int(a[0:4])
num2 = int(a[4:8])

revs_number1 = 0
revs_number2 = 0

while (num1 > 0):
    remainder = num1 % 10
    revs_number1 = (revs_number1 * 10) + remainder
    num1 = num1 // 10

while (num2 > 0):
    # Logic
    remainder = num2 % 10
    revs_number2 = (revs_number2 * 10) + remainder
    num2 = num2 // 10

if revs_number1 > revs_number2:
    print(revs_number1)
else:
    print(revs_number2)