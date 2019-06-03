import time
import urllib.request as rq


URL = "http://apache/?secret=battles{restrict_everything}"

while True:
    try:
        rq.urlopen(URL)
    except:
        print("No response")
    print("Sucess!")
    time.sleep(10)

