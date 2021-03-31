a = input()
month = a[0:3]
date = a[4:6]

if (month == 'OCT' and date == '31') or (month == 'DEC' and date == '25'):
    print('yup')
else:
    print('nope')