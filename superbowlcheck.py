import telegram_send
from datetime import datetime
import ssl
import requests
import subprocess
import urllib
import time
from bs4 import BeautifulSoup as bs

# setting the URL you want to monitor
url = 'https://www.nflshop.com/los-angeles-rams/jerseys/t-14481448+d-9060443446+z-97-2226888184'
kuppurl = 'https://www.nflshop.com/los-angeles-rams/mens-los-angeles-rams-cooper-kupp-nike-white-alternate-super-bowl-lvi-game-patch-jersey/t-25377037+p-8207050591938+z-9-2725090030?_ref=p-DLP:m-GRID:i-r0c1:po-1'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}

#5241522571:AAFuX3r--RjvCsnLznD0EC9StNCYTFVWyGs
proxies = {
    'http://64.227.62.123:80',
    'http://147.135.255.62:8122',
    'http://188.166.206.183:8118',
    'http://167.172.203.244:8118',
    'http://167.99.163.146:3128',
    'http://142.93.16.163:3128',
    'http://50.233.228.147:8080',
    'http://66.170.183.90:9090',
    'http://191.243.217.1:53281',
    'http://165.22.59.84:8080',
    'http://157.230.255.230:8118'
}



# to create the initial hash
#currentHash = BeautifulSoup(response.content, 'html5lib')
#telegram_send.send(messages=["I've Started"])
requests.post('https://api.telegram.org/bot5241522571:AAFuX3r--RjvCsnLznD0EC9StNCYTFVWyGs/sendMessage?chat_id=5202978353&text=I''ve Started!')

print("running")
time.sleep(10)
while True:
    try:
        
        # perform the get request and store it in a var
        response = requests.get(url, headers=headers)
        kuppresponse = requests.get(kuppurl, headers=headers)
       
        # to create the initial hash
        soup = bs(response.content, 'html5lib')
        currentState = soup.find_all('div', class_='page-count')
        
        
        kuppsoup = bs(kuppresponse.content, 'html5lib')
        kuppcurrentState = kuppsoup.find_all('span', class_='stock-availability')


        print(currentState)
        print(kuppcurrentState)
        # wait for 30 seconds
        time.sleep(120)

        # perform the get request
        response = requests.get(url, headers=headers)
        kuppresponse = requests.get(kuppurl, headers=headers)


        soup = bs(response.content, 'html5lib')

        newState = soup.find_all('div', class_='page-count')


        kuppsoup = bs(kuppresponse.content, 'html5lib')
        kuppnewState = kuppsoup.find_all('span', class_='stock-availability')
        

        print(newState)
        print(kuppnewState)

        # check if new hash is same as the previous hash
        if currentState == newState:
            now = datetime.now()
            print('The Same =', now)
            
            
        # if something changed in the hashes
        else:
            # notify
            requests.post('https://api.telegram.org/bot5241522571:AAFuX3r--RjvCsnLznD0EC9StNCYTFVWyGs/sendMessage?chat_id=5202978353&text=Go check now!')
            print("something changed")

            # wait for 30 seconds
           

        # check if new hash is same as the previous hash
        if kuppcurrentState == kuppnewState:
            now = datetime.now()
            print('Kupp Same =', now)
           
            continue

        # if something changed in the hashes
        else:
            # notify
            requests.post('https://api.telegram.org/bot5241522571:AAFuX3r--RjvCsnLznD0EC9StNCYTFVWyGs/sendMessage?chat_id=5202978353&text=Go check Kupp now!')
            print("Kupp changed")

            # wait for 30 seconds
            time.sleep(120)
            continue

        

    # To handle exceptions
    except Exception as e:
        requests.post('https://api.telegram.org/bot5241522571:AAFuX3r--RjvCsnLznD0EC9StNCYTFVWyGs/sendMessage?chat_id=5202978353&text=Bot Died')

        print("error")
        print(e)
