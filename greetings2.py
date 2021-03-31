str = input()
count = 0
for char in str:
    if char == "e":
        count += 1
a = int(count)  
print("h" + a*2*"e" + "y")