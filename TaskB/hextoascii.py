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
    


