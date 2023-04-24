from stock_data_service.dao.stock_data_dao import StockDataDao


#  Service层负责对dao层的数据进行处理
class StockDataService:
    def __init__(self):
        self.dao = StockDataDao()
    def get_stock_detail(self, code):
        return self.dao.get_stock_detail(code)

    def get_kline(self,code):
        return self.dao.get_kline(code)

    def get_capital_history(self, code):
        return self.dao.get_capital_history(code)

    def get_margin(self, code):
        return self.dao.get_margin(code)

    def get_indicator(self, code):
        return self.dao.get_indicator(code)

    def get_hodernum(self, code):
        return self.dao.get_holdernum(code)

    def get_index_perf(self,code):
        return self.dao.get_index_perf(code)





