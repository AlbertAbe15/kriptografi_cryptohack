import string

data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
decoded = bytearray.fromhex(data)


flag = ''
for i in range(256):
    for w in decoded:
        flag += chr(w ^ i)

    if ('crypto' in flag):
        print(flag)
    flag = ''