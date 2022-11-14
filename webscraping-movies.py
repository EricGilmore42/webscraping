
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


url = 'https://www.boxofficemojo.com/year/2022/'


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

tables = soup.findAll('table')


row = tables[0]

tr = row.findAll('tr')

count = 1

for row in tr: 
    td = row.findAll('td')
    if td: 
        if count <= 5:
            rank = td[0].text
            name = td[1].text
            rev = td[7].text
            release = td[8].text
            dis = td[9].text
            theaters = td[6].text
            avg = float(rev.replace('$','').replace(',','')) / float(theaters.replace(',',''))

            print(f"Rank: {rank}")
            print(f"Name: {name}")
            print(f"Release Date: {release}")
            print(f"Total Gross: {rev}")
            print(f"Distributo: {dis}")
            print(f"Avg: {avg}")

            input()
            count +=1
