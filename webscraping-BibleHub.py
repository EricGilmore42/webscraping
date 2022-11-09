import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request





num = random.randint(1,21)

if num < 10: 
    webpage = 'https://biblehub.com/asv/john/'+ str(num) + '.htm'
else: 
    webpage = 'https://biblehub.com/asv/john/' + str(num) + '.htm'


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()
soup = BeautifulSoup(webpage,'html.parser')

page_verses = soup.findAll('p',class_='reg')

for verse in page_verses: 
    verse_list = verse.text.split('.')


myverse = 'Chatper: ' + str(num) + ' Verse:' + random.choice(verse_list[:len(verse_list)])

print(myverse)