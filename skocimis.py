e, f, c = map(int, input().split())

gap1 = f-e
gap2 = c-f

if gap1 > gap2:
    print(gap1 - 1)
else:
    print(gap2 - 1)