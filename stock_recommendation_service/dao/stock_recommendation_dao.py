import requests
import pywencai
class StockRecommendationDao:
    def __init__(self):
        self.filepath = '/data/recommendation.csv'
    def get_index_info(self,code):
        url = "http://localhost:5000/stock/getIndexPerf?code="+code
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers)
        print(response)

        if response.status_code == 200:
            data = response.json()
            return data

    def get_bio_stock(self):
        res = pywencai.get(question='所属同花顺行业包含医药生物且90集中度且市值大于300亿', query_type='stock')
        return res

    def get_con_stock(self):
        res = pywencai.get(question='所属同花顺行业包含食品饮料且90集中度且市值大于300亿', query_type='stock')
        return res



