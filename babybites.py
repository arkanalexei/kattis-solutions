who_cares = input()
string_split = str(input()).split()
countr = 1
result = 0
for i in string_split:
    if str(countr) == i or "mumble" == i:
        countr += 1
    else:
        result += 1
if result == 0:
    print("makes sense")
else:
    print("something is fishy")