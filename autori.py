string = input()
new_initials = []

for str in string:
    if str.isupper() == True:
        new_initials.append(str)

result = ''.join(new_initials)
print(result)
