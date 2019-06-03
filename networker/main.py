import socket
import threading
import random
import string
N = 50

class Listener(threading.Thread):

    def __init__(self, number, gen_str, port,  next_port, next_str):
        super(Listener, self).__init__()
        self.gen_str = gen_str
        self.number = number
        self.port = port
        self.next_port = next_port
        self.next_str = next_str

    def run(self):
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("0.0.0.0", self.port))
        s.listen(10)
        while True:
            a,b = s.accept()
            data = ""
            if self.number != 0:
                data = a.recv(500)
                data = data.strip()
            if self.number == 0 or data == self.gen_str:
                if self.number != N:
                    a.send("Connect at port %d and send \"%s\"" % (self.next_port, self.next_str))
                else:
                    a.send("Get_YOUR_flag: %s" % self.next_str)
            a.close()



def randstring(N):
    return "".join([random.choice(string.letters) for x in xrange(N)])

if __name__ == '__main__':
    ports = [31337]+ [10000 + random.randint(1000,10000) for i in xrange(N)]
    greet_strings = [""]+[randstring(15) for i in xrange(N)]
    params = zip(ports, greet_strings)
    print params
    x = zip(params, params[1:]+[(-1, "YZH_PO_GOLOVE_SEBE_POSTU4I")])
    print x
    counter = 0
    for i in x:
        portl = Listener(counter, i[0][1], i[0][0], i[1][0], i[1][1])
        portl.setDaemon(True)
        portl.start()
        counter += 1
    import time
    while(True):
        time.sleep(10)
