strink = str(input())
A_points = 0
B_points = 0
for i in range(len(strink)):
    if strink[i] == 'A':
        A_points += int(strink[i+1])
    elif strink[i] == 'B':
        B_points += int(strink[i+1])
    else:
        pass

if A_points > B_points:
    print("A")
else:
    print("B")