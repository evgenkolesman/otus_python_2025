def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


a = input()

if(is_int(a)):
    result = 0
    while (len(a) > 1):
        for dig in a:
            result += int(dig)
        a = str(result)
        result = 0
    print(a)
else: print("BAD DATA")
