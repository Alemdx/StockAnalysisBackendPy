import pysnowball as ball

# dao层获得数据
class StockDataDao:
    def __init__(self):
        self.filepath = '/data/stocks.csv'

# 获取股票详细数据
    def get_stock_detail(self, code):
        ball.set_token('xq_a_token = 80f8d831418bba697ce50569d95b51cbd92d8926')
        detail = ball.quote_detail(code)
        return detail

# 获取股票k线数据。附带天数
    def get_kline(self,code):
        ball.set_token('xq_a_token = 80f8d831418bba697ce50569d95b51cbd92d8926')
        detail=ball.kline(code,900)
        return detail
# 获取融资融券数据
    def get_margin(self,code):
        ball.set_token('xq_a_token = 80f8d831418bba697ce50569d95b51cbd92d8926')
        detail = ball.margin(code)
        return detail


#获取净流量大宗
    def get_capital_history(self,code):
        ball.set_token('xq_a_token = 80f8d831418bba697ce50569d95b51cbd92d8926')
        detail = ball.capital_history(code)
        return detail

#获取业绩数据(年报季报)
    def get_indicator(self,code):
        ball.set_token('xq_a_token = 80f8d831418bba697ce50569d95b51cbd92d8926')
        detail = ball.indicator(code)
        return detail

#获取股东人数
    def get_holdernum(self,code):
        ball.set_token('xq_a_token = 80f8d831418bba697ce50569d95b51cbd92d8926')
        detail = ball.holders(code)
        return detail

#获取指数收益
    def get_index_perf(self,code):
        ball.set_token('xq_a_token = 80f8d831418bba697ce50569d95b51cbd92d8926')
        detail = ball.index_perf_90(code)
        return detail







