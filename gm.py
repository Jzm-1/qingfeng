import requests
import time
import random

def gm(headers,data):
    num = '123456789'
    letter = 'qwertyuiopasdfghjklzxcvbnm'
    cipher = random.sample(letter,2) + random.sample(num,6)
    headers['cipher'] = ''.join(cipher)

    url = 'https://ssl.ptlogin2.qq.com/qq_safe/declassify'
    while 1:
        try:
            requests.post(url, headers=headers, data=data)
        except:
            time.sleep(1)
            continue
        else:
            break