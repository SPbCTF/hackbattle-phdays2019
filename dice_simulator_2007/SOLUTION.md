На видео: [2:36:16](https://vk.com/video-114366489_456239197?t=2h36m16s)

Цель: Купить флаг от имени богатого юзера<br>

Функционал: <br>
  Страница с кубиками: можно бросить кубик против бота, у которого кубик имеет только  3 грани 4,5,6.<br>
  Страница о юзере: можно посмотреть инфо о юзере и купить флаг.<br>

Регистрируемся на сайте.<br>
Заходим во вкладку о юзере.<br>
Нажимаем кнопку купить флаг, перехватываем запрос: <br>

*POST /handle_data HTTP/1.1<br>
Host: 192.168.88.254:5000<br>
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0<br>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8<br>
Accept-Language: en-US,en;q=0.5<br>
Accept-Encoding: gzip, deflate<br>
Content-Type: application/x-www-form-urlencoded<br>
Content-Length: 16<br>
Connection: close<br>
Referer: http://192.168.88.254:5000/about_user<br>
Cookie: session=token<br>
Upgrade-Insecure-Requests: 1<br>
user=kukuxumushi*<br>

Для покупки флага необходимо иметь 1000 монеток, а у юзера 100 при регистрации. Для решения этой проблемы можно либо играть в кубики и попытатсья выгирать, либо посмотреть на запрос отправляемый, видим в теле POST запроса "user=kukuxumushi", вероятно сервер не проверяет легитимность запроса. <br>
Для получения флага можно заменить username на какой-нибудь другой популярный, например root, admin, user, test, administrator.<br>
После подмены запроса получаем редирект на страницу с флагом: flag is flag{d0_n0t_s7ea1_fr0m_SPbCTF_cru3l_ARSIB}.
