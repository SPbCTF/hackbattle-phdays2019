На видео: [3:36:17](https://vk.com/video-114366489_456239197?t=3h36m17s)

Для решения таска нужно попнуть alert('SPbCTF'), не используя консоль браузера. На страницу рефлектится параметр `spbctf`, но банальной экплуатации мешает CSP (Content Security Policy), который запрещает встраивать `inline` скрипты, а `script src` можно сделать только с любого поддомена гугла. 

Немного погуглив `csp bypass` можно найти, что в таком случае можно воспользоваться jsonp эндпоинтами, которые можно найти в том же гугле :).
Можно использовать дорки а-ля `inurl:"callback"` или `inurl:"jsonp"`

Для эндпоинта, который использован для авторского решения, нельзя использовать строки в явном виде. Чтобы обойти это, можно использовать трюк с `/string/.source` или воспользоваться функцией `String.fromCharCode()` (есть онлайн генератор https://jdstiles.com/java/cct.html)

Крутой доклад про обходы CSP: https://2018.zeronights.ru/wp-content/uploads/materials/3%20ZN2018%20WV%20-%20CSP%20bypass.pdf

Пример решения: `?spbctf=<script src="https://www.google.com/complete/search?client=chrome%26jsonp=alert(/spbctf/.source)//"></script>`
