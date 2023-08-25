# 下載 台灣第一銀行的匯率資料
# 並且將資料存入csv檔案

import global_variable as gv
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

def get_first_bank_exchange_rate():
    response = requests.get('https://ibank.firstbank.com.tw/NetBank/7/0201.html?sh=none', verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    currency = soup.find_all('td', class_='ListTitleFont')
    currency_name = []
    for i in currency:
        currency_name.append(i.text.strip())
    
    df = pd.DataFrame()
    df['幣別'] = currency_name[1::5]
    df['現金/即期'] = currency_name[2::5]
    df['買入匯率'] = currency_name[3::5]
    df['賣出匯率'] = currency_name[4::5]
    print(df)

    # 把匯率寫入 csv
    df.to_csv('first_bank_exchange_rate.csv', index=False, encoding='utf-8-sig')

get_first_bank_exchange_rate()