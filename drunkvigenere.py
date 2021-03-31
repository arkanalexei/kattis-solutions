# I copied the original vignere cipher code from www.geeksforgeeks.org/vigenere-cipher/
msg = str(input())
keys = str(input())

def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        if i % 2 == 0:
            x = (ord(string[i]) -
             ord(key[i])) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        else:
            x = (ord(string[i]) +
             ord(key[i])) % 26
            x += ord('A')
            cipher_text.append(chr(x))
    return("" . join(cipher_text))

print(cipherText(msg,keys))