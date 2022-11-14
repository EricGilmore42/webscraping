from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


import keys
from twilio.rest import Client

client = Client(keys.accountSID, keys.authToken)

TwilioNumber = "+14247229562"
myNumber = "+19727579033"
                 

url = 'https://cryptotracker.com/'


# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

tables = soup.findAll('tbody')

row = tables[0]

tr = row.findAll('tr')

count = 1 

for row in tr:
    td = row.findAll("td")
    if td:
        a = row.findAll('a')
        small = row.findAll('small')
        if count <=5: 
            coin = a[0].text
            sym = small[0].text
            price = td[3].text
            change = td[4].text
            print(f"Coin name: {coin} ({sym})") 
            print(f"Percent Change: {change}")
            print(f"Price: {price}")
            if '-' in change:
                c_amt = float(price.replace('$','').replace(',','')) * float('.' + (change.replace('-','').replace('.','').replace('%','')))
                c_price = float(price.replace('$','').replace(',','')) + float(c_amt)
                print(f"Corresponding Price: ${format(c_price,',.2f')}")
            elif '+' in change:
                c_amt = float(price.replace('$','').replace(',','')) * float('.' + (change.replace('+','.').replace('.','').replace('%','')))
                c_price = float(price.replace('$','').replace(',','')) - float(c_amt)
                print(f"Corresponding Price: ${format(c_price,',.2f')}")
            input()
    if coin == 'Bitcoin' and float(price.replace('$','').replace(',','')) < 40000:
        textmsg = client.messages.create(to=myNumber,from_=TwilioNumber,body=f'Alert: Bitcoin has fallen below $40,000. Current price is {price}.')
        print(textmsg.status)
    if coin == 'Ethereum' and float(price.replace('$','').replace(',','')) < 3000:
        textmsg = client.messages.create(to=myNumber,from_=TwilioNumber,body=f'Alert: Ethereum has fallen below $3,000. Current price is {price}.') 
        print(textmsg.status)   
    count += 1


