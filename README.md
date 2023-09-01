# 銀行匯率抓取工具

本專案提供三個 Python 腳本，用於抓取不同銀行的匯率資訊，並將其儲存為 CSV 格式。

## 支持的銀行列表

- 台灣銀行
- 第一銀行
- 合作金庫銀行

## 使用方法

### 環境設置

1. 安裝 Python 3.x
2. 安裝必要的依賴包
    1. beautifulsoup4
    2. requests
    3. pandas

### 執行腳本

#### 抓取台灣銀行的匯率 [code](taiwan_bank_exchange_rate.py)

```bash
python taiwan_bank_exchange_rate.py
```

#### 抓取第一銀行的匯率 [code](first_bank_exchange_rate.py)
```bash
python first_bank_exchange_rate.py
```

#### 抓取合作金庫銀行的匯率 [code](taiwan_cooperative_bank_exchange_rate.py)
```bash
python taiwan_cooperative_bank_exchange_rate.py
```

#### 輸出格式

每一個爬蟲腳本均會獨立生成一份 CSV 文件，專門用於詳細列舉相關的匯率資料。這些 CSV 文件會包含以下五個主要欄位：

- **幣別（Currency Code）**: 用於明確表示貨幣種類的名稱或代碼，如：USD、EUR。
- **現金買入匯率（Cash Buying Rate）**: 顯示該貨幣目前的買入價格。
- **現金賣出匯率（Cash Selling Rate）**: 揭示該貨幣目前的賣出價格。
- **即期買入匯率（Spot Buying Rate）**: 表示該貨幣在即期市場上的當前買入價格。
- **即期賣出匯率（Spot Selling Rate）**: 指出該貨幣在即期市場上的當前賣出價格。

這樣的格式設計旨在提供全面而易於理解的匯率資訊。

#### 授權

本專案採用MIT授權協議，詳情請參閱隨附的 [LICENSE](LICENSE) 文件。
MIT授權協議是一個寬鬆的授權協議，允許用戶自由使用、修改和分發原始或衍生作品，但必須注明原作者的版權信息。