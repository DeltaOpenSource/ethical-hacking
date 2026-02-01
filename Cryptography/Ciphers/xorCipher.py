def encode_xor(txt: str, key: str) -> bytes:
    txt_representation = txt.encode('utf-8')
    key_representation = key.encode('utf-8')

    result = bytearray()

    for i in range(len(txt)):
        txt_byte = txt_representation[i]
        key_byte = key_representation[i % len(key_representation)]
        xor_byte = txt_byte ^ key_byte

        result.append(xor_byte)
    return result
    
def decode_xor(en_txt: bytes, key: str) -> str:
    key_representation = key.encode('utf-8')

    result = bytearray()

    for i in range(len(en_txt)):
        entxt_byte = en_txt[i]
        key_byte = key_representation[i % len(key_representation)]
        xor_byte = entxt_byte ^ key_byte

        result.append(xor_byte)
    return result.decode('utf-8')

if __name__ == "__main__":
    text = input("[*] Input text: ")
    key = input("[*] Input key: ")
    encoded_text = encode_xor(text, key)
    print(f"[*] Encoded (hex): {encoded_text.hex()}")
    decoded_text = decode_xor(encoded_text, key)
    print(f"[*] Decoded: {decoded_text}")
