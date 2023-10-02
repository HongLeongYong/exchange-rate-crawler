# 下載 台灣第一銀行的匯率資料
# 並且將資料存入csv檔案

import global_variable as gv
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# get first bank exchange rate
def main():
    has_proxy_bool = gv.has_proxy

    if has_proxy_bool:
        success_bool = False
        lv_timeout = 1
        while not success_bool:
            for p in gv.proxy:
                try:
                    response = requests.get('https://ibank.firstbank.com.tw/NetBank/7/0201.html?sh=none', proxies=p, verify=False, timeout=lv_timeout)
                    print('success: ' + p['https'])
                    success_bool = True
                except:
                    print('failed: ' + p['https'])
            lv_timeout += 1
    else:    
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
    
    pivot_df = df.pivot(index='幣別', columns='現金/即期', values=['買入匯率', '賣出匯率'])
    # 重設欄位名稱
    pivot_df.columns = ['_'.join(col) for col in pivot_df.columns]
    # 重置 index
    pivot_df.reset_index(inplace=True)
    pivot_df.columns = ['幣別', '現金買入匯率','即期買入匯率', '現金賣出匯率','即期賣出匯率']

    new_order = ['幣別', '現金買入匯率','現金賣出匯率', '即期買入匯率', '即期賣出匯率']
    pivot_df = pivot_df[new_order]

    print(pivot_df)
    # 把匯率寫入 csv
    df.to_csv('first_bank_exchange_rate.csv', index=False, encoding='utf-8-sig')

if __name__ == '__main__':
    main()  