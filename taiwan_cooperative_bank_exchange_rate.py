import requests
from bs4 import BeautifulSoup
import time

url = 'https://www.tcb-bank.com.tw/personal-banking/deposit-exchange/exchange-rate/spot'

session = requests.Session()

response = session.get(url)
cookies = (session.cookies.get_dict())
cookies_str = ';'.join([f"{key}={value}" for key, value in cookies.items()])
# print(cookies_str)

# response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser') 
token = soup.find('input',{'name':'__RequestVerificationToken'}).get('value')
# print(token)

payload = {
        '__RequestVerificationToken': token,
        'date': '2023-08-29',
        'time': '2'
    }

header = {
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding' : 'gzip, deflate, br',
'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Connection': 'keep-alive',
'Content-Length': '158',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': cookies_str ,
'Host': 'www.tcb-bank.com.tw',
'Origin': 'https://www.tcb-bank.com.tw',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest',
'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"'
}

click_url = 'https://www.tcb-bank.com.tw/api/client/ForeignExchange/GetSpotForeignExchangeSpecific'

response = requests.post(click_url, data = payload, headers= header)
print(response.json())
if response.status_code == 200:
    # 解析返回的內容
       soup = BeautifulSoup(response.content, 'html.parser')
    
    # 在這裡進行您的處理
else:
       print( response.status_code )
