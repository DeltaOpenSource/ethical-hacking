def rot13(message):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    listRot = []
    changesMessage = list(message)
    for index, txt in enumerate(changesMessage):
        if 'a' <= txt <= 'z':
            indexTxt = alphabet.index(txt)
            indexRot = indexTxt + 13
            try:
                listRot.append(alphabet[indexRot])
            except:
                listRot.append(alphabet[indexRot - 26])
        elif 'A' <= txt <= 'Z':
            indexTxt = alphabet.index(txt.lower()) 
            indexRot = indexTxt + 13
            try:
                a = alphabet[indexRot] 
                listRot.append(a.upper())
            except:
                b = alphabet[indexRot - 26] 
                listRot.append(b.upper())
        else:
            listRot.append(txt)
    return ''.join(listRot)

encoded = rot13("your text")
print(encoded)
