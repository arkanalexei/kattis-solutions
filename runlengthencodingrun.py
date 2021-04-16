command = input().split()

# Decode
dcode = command[1]
def decoding(string):
    encoded = ''
    nums = '1234567890'
    for i in range(len(dcode)):
        if dcode[i] not in nums:
            encoded += (int(dcode[i + 1]) * dcode[i])
    return encoded

# Encode
ncode = command[1]
def encoding(string):
    decoded = ''
    prev_char = ''
    count = 1
    for char in ncode:
        if char != prev_char:
            if prev_char:
                decoded += prev_char + str(count)
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        decoded += prev_char + str(count)
    return decoded

if command[0] == 'E':
    print(encoding(command[1]))
elif command[0] == 'D':
    print(decoding(command[1]))