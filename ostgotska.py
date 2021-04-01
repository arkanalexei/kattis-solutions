string = input().split()
countr = 0
for word in string:
    if 'ae' in word:
        countr += 1
if countr/len(string) * 10 >= 4:
    print("dae ae ju traeligt va")
else:
    print('haer talar vi rikssvenska')