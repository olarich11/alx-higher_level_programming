def remove_char_at(s, n):
    result = ""
    for i, c in enumerate(s):
        if i != n:
            result += c
    return result
