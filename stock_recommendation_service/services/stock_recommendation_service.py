from stock_recommendation_service.dao.stock_recommendation_dao import StockRecommendationDao
import json

class StockRecommendationService:
    def __init__(self):
        self.dao = StockRecommendationDao()

    def has_new_high(self, code, n):
        n_days = int(n)
        instance = StockRecommendationDao()
        data = instance.get_index_info(code)

        # 获取所有数据和最近n天数据
        all_data = data["data"]
        data_n_days = all_data[-n_days:]

        # 获取所有数据和最近n天数据的最高价列表
        all_high_prices = [item["high"] for item in all_data]
        n_days_high_prices = [item["high"] for item in data_n_days]

        # 计算所有数据和最近n天数据中最高价的最大值
        max_high_all_data = max(all_high_prices)
        max_high_n_days = max(n_days_high_prices)

        # 判断是否在最近n天达到了新高
        new_high = max_high_n_days == max_high_all_data

        return new_high

    def get_bio_stock(self):
        return self.dao.get_bio_stock()

    def get_con_stock(self):
        return self.dao.get_con_stock()



