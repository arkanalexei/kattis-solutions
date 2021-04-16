in_building = []
who_cares = int(input())
commands = []

while who_cares > 0:
    commands.append(str(input()))
    who_cares = who_cares - 1

names = []
for command in commands:
    namez = command.split()
    names.append(namez[1])

for name,i in zip(names,range(len(commands))):
    if 'entry' in commands[i] and name not in in_building:
        in_building.append(name)
        print(str(name) + " entered")
    elif 'entry' in commands[i] and name in in_building:
        print(str(name) + " entered (ANOMALY)")
    elif 'exit' in commands[i] and name in in_building:
        in_building.remove(name)
        print(str(name) + " exited")
    elif 'exit' in commands[i] and name not in in_building:
        print(str(name) + " exited (ANOMALY)")