def uppercase(s):
    result = ""

    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - ord('a') + ord('A'))
        else:
            result += char

    formatted_result = "{}".format(result)
    print(formatted_result)
