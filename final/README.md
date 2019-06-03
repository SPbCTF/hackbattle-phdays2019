# Финальный раунд

## Авторы
Артур Ханов ([awengar](https://github.com/awengar)), Андрей Бугаевский ([nUl1](https://github.com/nUl1)), Влад Росков ([v0s](https://github.com/v0s))

## Видео финала
[vk.com/video-114366489_456239197?t=4h02m20s](https://vk.com/video-114366489_456239197?t=4h02m20s)

## Задание
```
FoodShoot.exe, config.ini

--------------

chmod 0644 /home/imgstore/id_rsa
chmod 0755 /home/pwn/ ; chown root:root /home/pwn/pwn ; chmod 04755 /home/pwn/pwn
chmod 0755 /home/sysmon/ ; chown root:root /home/sysmon/suid_system_monitoring ; chmod 04755 /home/sysmon/suid_system_monitoring
chown root:root /home/flag/ ; chmod 0700 /home/flag/


Стадия 1:
REV — FoodShoot.exe, config.ini
WEB — /home/imgstore/ (SQLi)

Стадия 2:
WEB — /home/imgstore/ (читалка)
DATA — /home/imgstore/.git/

Стадия 3:
PWN — /home/pwn/
DATA — /home/sysmon/
```

## [Решение](SOLUTION.md)
