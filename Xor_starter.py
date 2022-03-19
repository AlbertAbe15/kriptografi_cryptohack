character = "label"
flag = ''

for c in character:
    flag += chr(ord(c) ^ 13)

print('crypto{{{}}}'.format(flag))