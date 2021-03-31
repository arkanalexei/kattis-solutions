name = input()
new_name = '' + name[0]
for i in range(len(name)-1):
    if name[i] != name[i+1]:
        new_name += name[i+1]

print(new_name)
