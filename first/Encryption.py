def encrypt(text, key):
    result = []
    key_length = len(key)
    key_index = 0

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            keys = key[key_index % key_length]
            if(key_length == 0): keys = "a"
            shift = ord(keys.lower()) - ord('a')
            shifted_char = chr(start + (ord(char) - start + shift) % 26)
            result.append(shifted_char)
            key_index += 1
        else:
            result.append(char)

    return ''.join(result)

text = input("Enter a string: ")
key = input("Enter a key: ")

print("Encrypted value: ", encrypt(text, key))
