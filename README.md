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

    ```bash
    pip install beautifulsoup4
    ```

### 執行腳本

#### 抓取台灣銀行的匯率

```bash
python taiwan_bank_exchange_rate.py
```

#### 抓取第一銀行的匯率
```bash
python first_bank_exchange_rate.py
```

#### 抓取合作金庫銀行的匯率
```bash
python taiwan_cooperative_bank_exchange_rate.py
```

#### 輸出格式

每個腳本會獨立生成一個CSV文件，用以詳細列出匯率資料。每個CSV文件將會包含以下三個主要欄位：

- **貨幣類型**：指明了貨幣的名稱或代碼（例如：USD, EUR）。
- **買入價格**：該貨幣目前的買入價格。
- **賣出價格**：該貨幣目前的賣出價格。

這些資料有助於用戶快速了解各種貨幣的匯率狀況。

#### 授權

本專案採用MIT授權協議，詳情請參閱隨附的 [LICENSE](LICENSE) 文件。
MIT授權協議是一個寬鬆的授權協議，允許用戶自由使用、修改和分發原始或衍生作品，但必須注明原作者的版權信息。