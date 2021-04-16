while True:
    sides = [int(x) for x in input().split()]
    hypotenuse = max(sides)
    sides.remove(hypotenuse)
    if hypotenuse == 0:
        break
    if hypotenuse ** 2 == (sides[0] ** 2 + sides[1] ** 2):
        print("right")
    else:
        print("wrong")