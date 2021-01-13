import requests
from bs4 import BeautifulSoup
from io import StringIO
import json
import csv
from datetime import datetime, timedelta
import time 

def getData(symbol):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36' }

    url = f'https://finance.yahoo.com/quote/{symbol}'




    r = requests.get(url, headers= header)


    soup = BeautifulSoup(r.text, 'html.parser')


    #Elements 
    stock = { 
            'name' : soup.find('h1', {'class': 'D(ib) Fz(18px)'}).text,
           ' price ': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[0].text,
            'change ': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[1].text,
            'day_range' : soup.find('td', {'data-test': 'DAYS_RANGE-value'}).text
           }
    
 
    
    return stock

def getHistoricData(symbol):
    
    url_financails = f'https://query1.finance.yahoo.com/v7/finance/download/{symbol}'

    params = {
        'range' : '1y',
        'interval' : '1d',
        'events' : 'history'
    }


    response = requests.get(url_financails, params=params)
    
    file = StringIO(response.text)
    reader = csv.reader(file)
    next(reader)
    data = {'chartData' : []}
    for row in reader:
        data['chartData'].append({
            'date': row[0],
            'open': row[1],
            'high': row[2],
            'low' : row[3],
            'close': row[4],
            'adj' : row[5],
            'volume' : row[6]
            
        })
    
    return data
  
flag = False



while 1:
    
    mystocks = ['PLUG' ]
    stockdata = []
    for stock in mystocks:
        stockdata.append(getData(stock))
        stockdata.append(getHistoricData(stock))
        print('Getting:' , stock)
        
    with open('stockdata.json' , 'w') as f:
        json.dump(stockdata, f, indent=4)
        
    print('Done')
    
    dt = datetime.now() + timedelta(seconds=5)
    

    while datetime.now() < dt:
        time.sleep(1)

    


    




