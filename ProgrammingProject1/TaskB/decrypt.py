import math
import BigNumber

# public key is {e, n}
# private key is {d, n}

def gcd(a,b):
    return gcd(b,a%b)

def encrypt(me, e, n):
    en = me**e
    c = en % n
    print("Encrypted Message is: ", c)
    return c

def hexToDec(temp):
    a = ""
    for i in range(len(temp)):
        a = a + str(temp[-i-1])

    t = 0
    for i in range(len(a)):
        if a[i] == "A":
            t += (16**i)*10
        elif a[i] == "B":
            t += (16**i)*11
        elif a[i] == "C":
            t += (16**i)*12
        elif a[i] == "D":
            t += (16**i)*13
        elif a[i] == "E":
            t += (16**i)*14
        elif a[i] == "F":
            t += (16**i)*15
        else:
            t += (16**i)*int(a[i])
    return t

def decToHex(temp, stringy):
    if temp%16 == 0:
        for i in range(len(stringy)):
            stringy = stringy + str(temp[-i-1])
        return stringy
    else:
        stringy = stringy + str(temp%16)
        return decToHex(temp%16, stringy)

def B1():
    # this is for B.1
    message = int(input("Enter the message to be encrypted: ")) 
 
    p = "F7E75FDC469067FFDC4E847C51F452DF"
    q = "E85CED54AF57E53E092113E62F436F4F"
    e = "0D88C3"

    p = hexToDec(p)
    q = hexToDec(q)
    e = hexToDec(e)
    
    n = p*q

    print("Original Message is: ", message)
    c = encrypt(message, e, n)

    print("p =", str(p), "\nq =", str(q), "\ne =", str(e))

    n = p*q
    k = (p-1)*(q-1)

    print("n =", str(n), "\nk =", str(k))

    d = (k+1) / e

    print("d =", d)

def B2():
    # This is for B.2
    # Givens
    n = "DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5"
    e = "010001" 
    e_dec = 65537
    m = "A top secret!"
    d = "74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D"
    c = "8C0F971DF2F3672B28811407E2DABBE1DA0FEBBBDFC7DCB67396567EA1E2493F"

    hex_topsecret = '0x1420ee57e0eb129c5295067005491'



    cyphertext = '2fa9e6d84781da2417d8c46632fe29bb'

    # Make an array of the ascii values of the message (m)
    mess = ""
    for i in range(len(m)):
        mess = mess + str(ord(m[i]))

    # Take the array and make it an array of hex values
    hexMess = hex(int(mess))

    n = int(n, 16)
    d = int(d, 16)
    c = int(c, 16)
    # use the ascii values of the characters of the message to encrypt
    # "mess" is a string of ints here
    cypher = (int(mess)**e_dec) % n
    print("Encrypted Message is: ", cypher)

    # string Cypher doesn't work correctly bc Ascii can be 1,2, or 3 nums long
    stringCypher = str(cypher)


    # this is where the decryption should take place
    messager = c**d
    messager = messager % n
    print("Decrypted message is: ", messager)
    print(c)

def B3():
    # Givens
    n = "DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5"
    e = "010001" 
    e_dec = 65537
    d = "74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D"
    c = "8C0F971DF2F3672B28811407E2DABBE1DA0FEBBBDFC7DCB67396567EA1E2493F"
    n = int(n, 16)
    d = int(d, 16)
    c = int(c, 16)
    m = "I owe you $2000"

    mess = ""
    for i in range(len(m)):
        mess = mess + str(ord(m[i]))

    cypher = int(mess)**e_dec % n
    print("Encrypted Message 1 is: ", cypher)

    m = "I owe you $3000"

    mess = ""
    for i in range(len(m)):
        mess = mess + str(ord(m[i]))

    cypher = int(mess)**e_dec % n
    print("Encrypted Message 2 is: ", cypher)

    m = "Launch a missile"
    s = "643D6F34902D9C7EC90CB0B2BCA36C47FA37165C0005CAB026C0542CBDB6802F"
    n = "AE1CD4DC432798D933779FBD46C6E1247F0CF1233595113AA51B450F18116115"
    s = int(s, 16)
    e_dec = 65537
    n = int(n, 16)
    mess = ""
    for i in range(len(m)):
        mess = mess + str(ord(m[i]))

    cypher = int(mess)**e_dec % n
    print("Encrypted Message 2 is: ", cypher)

    print(cypher == s)
    print(cypher, "\n", s)

    s = "643D6F34902D9C7EC90CB0B2BCA36C47FA37165C0005CAB026C0542CBDB6803F"
    s = int(s, 16)
    print(cypher == s)
    print(s)

B2()
B3()