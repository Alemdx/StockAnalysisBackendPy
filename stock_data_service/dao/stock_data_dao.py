import pysnowball as ball
import pywencai
import pandas as pd

# dao层获得数据
class StockDataDao:
    def __init__(self):
        self.filepath = '/data/stocks.csv'

# 获取股票详细数据
    def get_stock_detail(self, code):
        ball.set_token('xq_a_token = f7308d753e8f1bf23cc9c32b3e66757d61a5a77c')
        detail = ball.quote_detail(code)
        return detail

# 获取股票k线数据。附带天数
    def get_kline(self,code):
        ball.set_token('xq_a_token = f7308d753e8f1bf23cc9c32b3e66757d61a5a77c')
        detail=ball.kline(code,900)
        return detail
# 获取融资融券数据
    def get_margin(self,code):
        ball.set_token('xq_a_token = f7308d753e8f1bf23cc9c32b3e66757d61a5a77c')
        detail = ball.margin(code)
        return detail


#获取净流量大宗
    def get_capital_history(self,code):
        ball.set_token('xq_a_token = f7308d753e8f1bf23cc9c32b3e66757d61a5a77c')
        detail = ball.capital_history(code)
        return detail

#获取业绩数据(年报季报)
    def get_indicator(self,code):
        ball.set_token('xq_a_token = f7308d753e8f1bf23cc9c32b3e66757d61a5a77c')
        detail = ball.indicator(code)
        return detail

#获取股东人数
    def get_holdernum(self,code):
        ball.set_token('xq_a_token = f7308d753e8f1bf23cc9c32b3e66757d61a5a77c')
        detail = ball.holders(code)
        return detail

#获取指数收益
    def get_index_perf(self,code):
        ball.set_token('xq_a_token = f7308d753e8f1bf23cc9c32b3e66757d61a5a77c')
        detail = ball.index_perf_90(code)
        return detail

# 获取指数成分股票
    def get_index_comp(self,code):
        ball.set_token('xq_a_token = f7308d753e8f1bf23cc9c32b3e66757d61a5a77c')
        detail=ball.index_weight_top10("399967")
        return detail

#获取A股成交额
    def get_Avolumn(self):
        res=pywencai.get(question='A股成交额', query_type='zhishu')
        # print(res["成交额"][0])
        return res["成交额"][0]

#获取美元对人民币
    def get_foreign(self):
        res = pywencai.get(question='人民币美元', query_type='foreign_exchange')
        return res["外汇@最新价"][1]

#同花顺热门概念
    def get_hot_notion(self):
        res=pywencai.get(question='同花顺概念指数中板块涨幅排名前10',query_type='zhishu')
        selected_columns = ['指数代码', '指数简称']
        selected_data = res.loc[:, selected_columns]


        # 数据处理
        data_dict = selected_data.to_dict(orient='records')
        formatted_data = []
        for i, d in enumerate(data_dict):
            formatted_data.append({
                'ID': i + 1,
                'code': d['指数代码'].split('.')[0],
                'name': d['指数简称'],
            })
        return formatted_data

#获取热门股票
    def get_hot_stock(self):
        res=pywencai.get(question='热门股票', query_type='stock')


        selected_columns = ['股票代码', '股票简称']
        selected_data = res.loc[:, selected_columns]

        # 数据处理
        data_dict = selected_data.to_dict(orient='records')
        formatted_data = []
        for i, d in enumerate(data_dict):
            formatted_data.append({
                'ID': i + 1,
                'code': d['股票代码'].split('.')[0],
                'name': d['股票简称'],
            })
        return formatted_data

#获取上证指数涨幅
    def get_ShIndex(self):
        res=pywencai.get(question='上证指数目前涨幅', query_type='zhishu')
        return res["涨跌幅"][0]








