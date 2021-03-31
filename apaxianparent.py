name = input().split()
first_name = name[0]
last_name = name[1]

if first_name[-2:] == 'ex':
    print(first_name + last_name)
elif first_name[-1] == 'e':
    print(first_name + 'x' + last_name)
elif first_name[-1] in ['a','i','u','o']:
    print(first_name[:-1] + 'ex' + last_name)
else:
    print(first_name + 'ex' + last_name)







