# ECB mode, password: mgssecurity
openssl enc -aes-128-ecb -pbkdf2 -in original.bmp -out p2ebc.bmp

# CBC mode, password: mgssecurity
openssl enc -aes-128-cbc -pbkdf2 -in original.bmp -out p2cbc.bmp

# grab header of original bmp
head -c 54 original.bmp > header

# grab body of ebc encoded bmp
tail -c +54 p2ebc.bmp > body

# combine to create new (ebc encoded) bmp
cat header body > original_ebc.bmp

# grab body of cbc encoded bmp
tail -c +54 p2cbc.bmp > body

# combine to create new (cbc encoded) bmp
cat header body > original_cbc.bmp


