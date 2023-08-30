import requests
from bs4 import BeautifulSoup
import time
from pandas import json_normalize
import pandas as pd
from datetime import datetime

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
now = datetime.now()
formatted_date = str(now.strftime("%Y-%m-%d"))

print(f'執行日期： {formatted_date}')
print('台灣合作金庫銀行即期匯率： 10點匯率')

payload = {
        '__RequestVerificationToken': token,
        'date': formatted_date,
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
# print(response.text)

if response.status_code == 200:
    # 解析返回的內容
    df = json_normalize(response.json(), 'result')
    selected_df = df[['CurrencyName', 'Type', 'PromptExchange', 'CashExchange']]
    pivot_df = pd.pivot_table(df, index='CurrencyName', columns='Type', values=['PromptExchange', 'CashExchange'], aggfunc='first', sort=False)
    # 重置索引
    pivot_df.reset_index(inplace=True)

    # 重命名欄位
    pivot_df.columns = ['CurrencyName', 'PromptBuy', 'PromptSell', 'CashBuy', 'CashSell']
    pivot_df.to_csv('taiwan_cooperative_bank_exchange_rate.csv', index=False)
    # print(pivot_df)
else:
    print( response.status_code )
