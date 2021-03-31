blimp1= input().split()
blimp2= input().split()
blimp3= input().split()
blimp4= input().split()
blimp5= input().split()
blimps = blimp1+blimp2+blimp3+blimp4+blimp5

correct_blimps = []
for blimp in blimps:
    if 'FBI' in blimp:
        correct_blimps.append(blimp)

output = [i+1 for i, item in enumerate(blimps) if item in correct_blimps]

if len(output) == 0:
    print('HE GOT AWAY!')
else:
    for num in output:
        print(num, " ", end="")
