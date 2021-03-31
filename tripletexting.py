name = str(input())
firsttext = name[:int(len(name) / 3)]
secondtext = name[int(len(name) / 3):int((len(name)) / 3) + int(len(name) / 3)]
thirdtext = name[int((len(name)) / 3) + int(len(name) / 3):int(len(name))]

if firsttext == secondtext or firsttext == thirdtext:
    print(firsttext)
else:
    print(secondtext)