import random
from math import gcd

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = pow(e, -1, phi)
    return ((e, n), (d, n))

def encrypt(pk, mensagem):
    key, n = pk
    msg_c = ""
    for letra in mensagem:
        k = (ord(letra) ** key) % n
        msg_c += chr(k)
    return msg_c

def decrypt(pk, mensagem):
    key, n = pk
    msg_d = ""
    for letra in mensagem:
        k = (ord(letra) ** key) % n
        msg_d += chr(k)
    return msg_d

p = valor de p
q = valor de q
public_key, private_key = generate_keypair(p, q)