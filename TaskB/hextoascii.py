import binascii

def stringToHex(s):
    return s.encode("utf-8").hex()

def hexToAscii(s):
    asciiStr = ""
    for i in range(0, len(s), 2):
        temp = s[i: i+2]
        temp = chr(int(temp, 16))
        asciiStr = asciiStr + temp 
    return asciiStr
    

#print(int('643D6F34902D9C7EC90CB0B2BCA36C47FA37165C0005CAB026C0542CBDB6802F', 16))



print(stringToHex('Launch a missile.'))


#print(hexToAscii('50617373776F72642069732064656573'))

