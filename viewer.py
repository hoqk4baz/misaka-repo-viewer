# Code by Dark_Enza
# Telegram Channel @dwstoree

import requests
import threading

M = "\033[34m"
Y = "\033[32m"
R = "\033[31m"

print(M+"  _____             _      ______                "+M)
print(M+" |  __ \           | |    |  ____|               "+M)
print(M+" | |  | | __ _ _ __| | __ | |__   _ __  ______ _ "+M)
print(M+" | |  | |/ _` | '__| |/ / |  __| | '_ \|_  / _` |"+M)
print(M+" | |__| | (_| | |  |   <  | |____| | | |/ / (_| |"+M)
print(M+" |_____/ \__,_|_|  |_|\_\ |______|_| |_/___\__,_|"+M)
print(R+" ‎Merhaba! Ben Python kullanıyorum.  TG: dark_enza"+R)
print("")

bundleid = input(Y+"Bundle İD GiR: "+Y)
print("")

urls = "http://shimajiron.php.xdomain.jp/count/ViewCount/add.php?id="+bundleid

headers = {
    "Host": "shimajiron.php.xdomain.jp",
    "Accept": "*/*",
    "User-Agent": "misaka/1 CFNetwork/1390 Darwin/22.0.0",
    "Accept-Language": "tr-TR,tr;q=0.9",
    "Connection": "keep-alive",
    "Accept-Encoding": "gzip, deflate",
}

count = 0
threadklidi = threading.Lock()

def istek_gonder():
    global count
    while True:
        response = requests.get(urls, headers=headers)
        with threadklidi:
            count += 1
            print(Y+f"{count} izlenme gönderildi", end='\r'+Y)

threads = []
for i in range(10):
    t = threading.Thread(target=istek_gonder)
    t.start()
    threads.append(t)
