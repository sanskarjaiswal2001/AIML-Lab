#Read the input strings and modify it as per the follwoing algorithm
#1. Replace every letter by its adjacent letter (a becomes b, b becomes c, z becomes a) All special characters should remain the same
#2. Capitalize every vowel in this new string

def modify_string(inp_string):
    mod_string = ""
    for i in inp_string:
        if i.isalpha():
            if i == 'z':
                mod_string = mod_string + 'a'
            else:
                mod_string = mod_string + chr(ord(i)+1)
        else:
            mod_string = mod_string + i
    for i in mod_string:
        if i in ['a','e','i','o','u']:
            mod_string = mod_string.replace(i,i.upper())
    return mod_string

print(modify_string("abcde"))