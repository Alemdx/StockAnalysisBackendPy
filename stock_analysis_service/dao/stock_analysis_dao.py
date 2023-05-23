import requests
import pandas as pd
class StockAnalysisDao:
    def __init__(self):
        self.filepath = '/data/analysis.csv'

    def get_kline(self,code):
        url = "http://localhost:5000/stock/getKline?code="+code
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data["data"]["item"], columns=data["data"]["column"])
            # 将时间戳转换为日期
            df['timestamp'] = pd.to_datetime(df['timestamp'] // 86400000 + 1, unit='D', origin='1970-01-01').dt.date
            return df

