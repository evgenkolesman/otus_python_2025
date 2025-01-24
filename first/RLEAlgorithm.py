def rle_compress(input_string):
    if not input_string:
        return ""

    result = []
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            result.append(f"{count}{input_string[i - 1]}")
            count = 1
    result.append(f"{count}{input_string[-1]}")

    return ''.join(result)

a = input("Enter value: ")
print(rle_compress(a))