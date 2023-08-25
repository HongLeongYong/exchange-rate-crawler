import global_variable as gv
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

def get_taiwan_bank_exchange_rate():
    response = requests.get('https://rate.bot.com.tw/xrt?Lang=zh-TW', verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    currency = soup.find_all('div', class_='visible-phone print_hide')
    currency_name = []
    for i in currency:
        currency_name.append(i.text.strip())
    # print(currency_name)

    currency_rate = soup.find_all('td', class_='rate-content-cash text-right print_hide')
    # 取出現金買入匯率
    cash_buy_rate_list = []
    for i in currency_rate:
        cash_buy_rate_list.append(i.text.strip())
    cash_buy_rate_list = cash_buy_rate_list[::2] 
    # print(cash_buy_rate_list)

    # 取出現金賣出匯率
    cash_sell_rate_list = []
    for i in currency_rate:
        cash_sell_rate_list.append(i.text.strip())
    cash_sell_rate_list = cash_sell_rate_list[1::2]
    # print(cash_sell_rate_list)

    currency_rate = soup.find_all('td', class_='rate-content-sight text-right print_hide')

    # 取出即期買入匯率
    spot_buy_rate_list = []
    for i in currency_rate:
        spot_buy_rate_list.append(i.text.strip())
    spot_buy_rate_list = spot_buy_rate_list[::2]
    # print(spot_buy_rate_list)

    # 取出即期賣出匯率
    spot_sell_rate_list = []
    for i in currency_rate:
        spot_sell_rate_list.append(i.text.strip())
    spot_sell_rate_list = spot_sell_rate_list[1::2]
    # print(spot_sell_rate_list)

    # 把匯率寫入 pandas
    df = pd.DataFrame()
    df['幣別'] = currency_name
    df['現金買入匯率'] = cash_buy_rate_list
    df['現金賣出匯率'] = cash_sell_rate_list
    df['即期買入匯率'] = spot_buy_rate_list
    df['即期賣出匯率'] = spot_sell_rate_list
    print(df)

    # 把匯率寫入 csv
    df.to_csv('taiwan_bank_exchange_rate.csv', index=False, encoding='utf-8-sig')

get_taiwan_bank_exchange_rate()