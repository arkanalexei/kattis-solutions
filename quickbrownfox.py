import string
alphabet = list(string.ascii_lowercase)

n = int(input())
def multi_input():
    dom = 0
    while dom != n:
        data = input()
        if not data: break
        yield data
        dom += 1
userInput = list(multi_input())

for words in userInput:
    sentence = words
    lower_sentence = sentence.lower()
    missing_letter = []
    for char in alphabet:
        if char not in lower_sentence:
            missing_letter.append(char)

    str_missing_letter = ""
    for letter in missing_letter:
        str_missing_letter += letter

    if len(missing_letter) == 0:
        print('pangram')
    else:
        print('missing ' + str_missing_letter)