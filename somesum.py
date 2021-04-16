n = int(input())
r = (1+n) * n / 2

if n % 2 == 1:
    print("Either")
elif n % 2 == 0 and r % 2 == 1:
    print("Odd")
else:
    print("Even")