from stock_data_service.dao.stock_data_dao import StockDataDao
import json


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

    def get_index_comp(self,code):
        print(self.dao.get_index_comp(code))
        json_data = json.dumps(self.dao.get_index_comp(code))
        data= json.loads(json_data)
        weight_list=data["data"]["weightList"]
        res=[]

        for item in weight_list:
            security_code = item["securityCode"]
            security_name = item["securityName"]
            weight = item["weight"]

            res.append({
                "securityCode": security_code,
                "securityName": security_name,
                "weight": weight
            })

        results_json = json.dumps(res, ensure_ascii=False)

        return results_json

    def get_Avolumn(self):
        return self.dao.get_Avolumn();

    def get_foreign(self):
        return self.dao.get_foreign();

    def get_hot_notion(self):
        return self.dao.get_hot_notion();

    def get_hot_stock(self):
        return self.dao.get_hot_stock();

    def get_ShIndex(self):
        return self.dao.get_ShIndex();





