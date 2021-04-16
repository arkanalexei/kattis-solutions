# This in an absolutely terrible solution. But it works!
lst = []
who_cares = int(input())
while who_cares > 0:
    lst.append(str(input()).split())
    who_cares = who_cares - 1


dicts = {}
for name,like,birth in lst:
    dicts.update({name: [int(like),birth]})

sorted_like = {}

for key,value in sorted(dicts.items(), key=lambda e: e[1][0], reverse=True):
    sorted_like.update({key: value})

temp = []
result = dict()

for key,val in sorted_like.items():
    if val[1] not in temp:
        temp.append(val[1])
        result[key] = val


print(len(result))
sorted_name = []

for key,val in result.items():
    sorted_name.append(key)

name_final = sorted(sorted_name)
for name in name_final:
    print(name)
