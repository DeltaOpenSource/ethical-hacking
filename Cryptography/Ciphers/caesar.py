import string

ALPHABET= list(string.ascii_lowercase)
result = []

text = input("[*] Input text: ")

for el in list(text):
    if el.isalpha():
        is_upper = el.isupper()
        index = ALPHABET.index(el.lower())
        next_el = ALPHABET[(index + 1) % len(ALPHABET)]
        if is_upper:
            result.append(next_el.upper())
        else:
            result.append(next_el)
    else:
        result.append(el)

print(''.join(result))
