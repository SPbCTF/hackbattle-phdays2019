import sys
import os

if __name__ == "__main__":
    m123 = os.path.basename(sys.argv[0])
    __import__(m123[:-3])
else:
    kek = __name__
    print(list(zip(kek[::-1][:11], "qe_qu qe_qa")))
    if sum([abs(ord(x[0])-ord(x[1])) for x in zip(kek[::-1][:11], "qe_qu qe_qa")]) != 0:
        print("Nope!")
        exit(0)
    if __name__[0] != 'U' or __name__[2:4] != 'i_' or __name__[1] != 'n':
        print("Nope!")
        exit(0)
    print("OK!Now say the flag loudly ;]")
