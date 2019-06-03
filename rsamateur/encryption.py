from Crypto.Util import number
import gmpy2

FLAG = "*****************"

def generate_rsa():
    while True:
        e = 65537
        p = number.getPrime(256)
        q = number.getPrime(256)
        n = gmpy2.mpz(p) * gmpy2.mpz(q)
        phi_n = gmpy2.mpz(p - 1) * gmpy2.mpz(q - 1)

        if gmpy2.gcd(phi_n, e) == 1:
            return n, e, phi_n

def encrypt_rsa(e, n, m):
    c = [gmpy2.powmod(ord(char),e,n) for char in m]
    c = list(map(str, c))
    return c

n, e, phi_n = generate_rsa()
encrypted = encrypt_rsa(e, n, FLAG)
f = open('encrypted.txt','w')
f.write(f'e = {e},\nN = {n},\nCiphertext = {" ".join(encrypted)}')
f.close()

