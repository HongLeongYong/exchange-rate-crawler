import requests
from bs4 import BeautifulSoup
from pandas import json_normalize
import pandas as pd
from datetime import datetime

# get taiwan cooperative bank exchange rate
def main():
    # 動態網頁： 需要處理 post request
    url = 'https://www.tcb-bank.com.tw/personal-banking/deposit-exchange/exchange-rate/spot'

    session = requests.Session()

    # 難點有2: 1. 需要處理 token 2. 需要處理 cookies
    response = session.get(url)
    website_string = BeautifulSoup(response.text, 'html.parser') 

    cookies = (session.cookies.get_dict())
    cookies_string = ';'.join([f"{key}={value}" for key, value in cookies.items()])

    token = website_string.find('input',{'name':'__RequestVerificationToken'}).get('value')

    run_date = str(datetime.now().strftime("%Y-%m-%d"))

    print(f'執行日期： {run_date}')
    print('台灣合作金庫銀行10點匯率')

    payload = {
            '__RequestVerificationToken': token,
            'date': run_date,
            'time': '2'
        }

    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '158',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': cookies_string ,
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

    post_request_url = 'https://www.tcb-bank.com.tw/api/client/ForeignExchange/GetSpotForeignExchangeSpecific'

    response = requests.post(post_request_url, data = payload, headers= header)

    if response.status_code == 200:
        # 解析返回的內容
        df = json_normalize(response.json(), 'result')
        selected_df = df[['CurrencyName', 'Type', 'CashExchange','PromptExchange']]
        pivot_df = pd.pivot_table(df, index='CurrencyName', columns='Type', values=['CashExchange','PromptExchange'], aggfunc='first', sort=False)
        pivot_df.reset_index(inplace=True)

        # 重命名欄位
        pivot_df.columns = ['幣別', '現金買入匯率', '現金賣出匯率', '即期買入匯率', '即期賣出匯率']

        pivot_df.to_csv('taiwan_cooperative_bank_exchange_rate.csv', index=False)
    else:
        print( response.status_code )

if __name__ == '__main__':
    main()