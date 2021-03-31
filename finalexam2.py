n = int(input())
def multi_input():
    dom = 0
    while dom != n:
        data = input()
        if not data: break
        yield data
        dom += 1

answers = list(multi_input())

counter = 0
for i in range(len(answers)-1):
    if answers[i] == answers[i+1]:
        counter += 1
print(counter)