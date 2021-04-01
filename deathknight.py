who_cares = int(input())
moves = []
countr = 0

while who_cares > 0:
    moves.append(str(input()))
    who_cares = who_cares - 1

for move in moves:
    if 'CD' not in move:
        countr += 1
print(countr)