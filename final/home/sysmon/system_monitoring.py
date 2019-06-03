#!/usr/bin/python

N = 0x00eaead59b8021ecf13547d11a3dced91a8d84a5d2ee36a4ef0baec7a828f6930c06da97d8dc4eebeeb2d7b22d915762b2278f878eab356bbc43b5c153c4a1d071
e = 0x10001

def str2num(s):
    return int(s.encode("hex"), 16)

def num2str(n):
    s = hex(n)[2:].rstrip('L')
    if len(s) % 2 == 1:
        s = "0" + s
    return s.decode("hex")

def check_rsa_signature(data, sig):
    global N, e
    m = pow(sig, e, N)
    return m == str2num(data)
    

import os, sys, base64

if os.getuid() != 0:
    print r'/!\ This program is designed to run as SUID root'

if len(sys.argv) <3:
    print "USAGE: %s 'command' 'signature'"%sys.argv[0]
    exit()

cmd = sys.argv[1]
sig = base64.b64decode(sys.argv[2])

if not check_rsa_signature(cmd, str2num(sig)):
    print "Wrong signature!"
    exit()
    
print "[+] Security check passed"
os.system(cmd)
