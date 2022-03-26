def modularArithmetic2(base, exp, prime):
    if exp == prime:
        return base
    elif (base % prime != 0 ) & (exp + 1 == prime):
        return 1
    else:
        return -1

print(modularArithmetic2(273246787654, 65536, 65537))