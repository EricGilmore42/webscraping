import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request





num = random.randint(1,21)

if num < 10: 
    webpage = 'https://ebible.org/asv/JHN' + '0' + str(num) + '.htm'
else: 
    webpage = 'https://ebible.org/asv/JHN' + str(num) + '.htm'


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()
soup = BeautifulSoup(webpage,'html.parser')

page_verses = soup.findAll('div',class_='main')

for verse in page_verses: 
    verse_list = verse.text.split('.')


myverse = 'Chatper: ' + str(num) + ' Verse:' + random.choice(verse_list[:len(verse_list)-2])

print(myverse)