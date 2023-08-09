#!/usr/bin/python3
def to_uper(character):
    if ord(character) >= 97 and ord(character) <= 122:
        return chr(ord(character) - 32)
    else:
        return character

def uppercase(string):
    string_new = ""
    for char in string:
        string_new += to_uper(char)
    return string_new
