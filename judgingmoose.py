numbers = input().split()
new_numbers = []
for num in numbers:
    new_numbers.append(int(num))

sorted_nums = sorted(new_numbers)

tines = sorted_nums[1] * 2

if sorted_nums[1] == 0:
    print("Not a moose")
elif sorted_nums[0] != sorted_nums[1]:
    print("Odd " + str(tines))
elif sorted_nums[0] == sorted_nums[1]:
    print("Even " + str(tines))
