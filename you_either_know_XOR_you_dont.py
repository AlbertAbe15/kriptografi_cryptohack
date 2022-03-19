data = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
decode = bytes.fromhex(data)

output = b''
for b1, b2 in zip(decode[:7], "crypto{".encode()):
    output += bytes([b1 ^ b2])

output = output.decode("utf-8")

key = (output + "y").encode()
key += (key * int((len(decode) - len(key))/len(key)))[:((len(decode) - len(key))%len(key))]
key += key[:((len(decode) - len(key))%len(key))]

output = b''
for b1, b2 in zip(decode, key):
    output += bytes([b1 ^ b2])

output = output.decode("utf-8")
print(output)



