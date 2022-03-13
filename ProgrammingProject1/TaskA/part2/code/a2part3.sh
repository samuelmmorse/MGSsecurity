# ECB mode, password: mgssecurity
openssl enc -aes-128-ecb -pbkdf2 -in gypsy.bmp -out p2ebc_2.bmp

# CBC mode, password: mgssecurity
openssl enc -aes-128-cbc -pbkdf2 -in gypsy.bmp -out p2cbc_2.bmp

# grab header of original bmp
head -c 54 gypsy.bmp > header

# grab body of ebc encoded bmp
tail -c +54 p2ebc_2.bmp > body_gypsy_ebc

# combine to create new (ebc encoded) bmp
cat header body_gypsy_ebc > gypsy_ebc.bmp

# grab body of cbc encoded bmp
tail -c +54 p2cbc_2.bmp > body_gypsy_cbc

# combine to create new (cbc encoded) bmp
cat header body_gypsy_cbc > gypsy_cbc.bmp


