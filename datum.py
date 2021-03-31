import datetime
day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

userinput = input().split()
month = int(userinput[1])
dayy = int(userinput[0])

day = datetime.datetime(2009,month,dayy).weekday()
print(day_name[day])