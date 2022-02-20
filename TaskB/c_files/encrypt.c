/* bn_sample.c */
#include <stdio.h>
#include <openssl/bn.h>
#define NBITS 256
void printBN(char *msg, BIGNUM * a) {
    /* Use BN_bn2hex(a) for hex string
    * Use BN_bn2dec(a) for decimal string */
    char * number_str = BN_bn2hex(a);
    printf("%s %s\n", msg, number_str);
    OPENSSL_free(number_str);
}


int main () {

    BN_CTX *ctx = BN_CTX_new();
    BIGNUM *m = BN_new();
    BIGNUM *e = BN_new();
    BIGNUM *n = BN_new();
    BIGNUM *res = BN_new();

    // Initialize a, b, n
    BN_hex2bn(&m, "4c61756e63682061206d697373696c652e");
    BN_dec2bn(&e, "65537");
    BN_hex2bn(&n, "AE1CD4DC432798D933779FBD46C6E1247F0CF1233595113AA51B450F18116115");

    // res = a*b
    //BN_mul(res, m, e, ctx);
    //printBN("a * b = ", res);

    // res = aˆb mod n
    BN_mod_exp(res, m, e, n, ctx);
    printBN("m^e mod n = ", res);

    BIGNUM *h = BN_new();
    h = res;
    BIGNUM *d = BN_new();
    BN_hex2bn(&d, "74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D");


    BN_mod_exp(res, h, d, n, ctx);
    printBN("h^d mod n = ", res);

    return 0;
}
