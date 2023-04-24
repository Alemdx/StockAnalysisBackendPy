from flask import Blueprint, jsonify, request
from stock_data_service.services.stock_data_service import StockDataService


stock_blueprint = Blueprint('stocks', __name__)

# 获取股票详情
@stock_blueprint.route('/stock/getOneDetail', methods=['POST'])
def get_stock_detail():
    code = request.args.get('code')
    instance = StockDataService()
    detail = instance.get_stock_detail(code)
    return jsonify(detail)

# 获取k线数据
@stock_blueprint.route('/stock/getKline', methods=['POST'])
def get_kline():
    code = request.args.get('code')
    instance = StockDataService()
    kline = instance.get_kline(code)
    return jsonify(kline)

# 获取主力资金净流入数据  能查看每日，总共20天
@stock_blueprint.route('/stock/getCapitalHsitory', methods=['POST'])
def get_capital_history():
    code = request.args.get('code')
    instance = StockDataService()
    capital_history = instance.get_capital_history(code)
    return jsonify(capital_history)

#获取融资融券数据
@stock_blueprint.route('/stock/margin', methods=['POST'])
def get_margin():
    code = request.args.get('code')
    instance = StockDataService()
    margin = instance.get_margin(code)
    return jsonify(margin)

#获取业绩数据
@stock_blueprint.route('/stock/getIndicator', methods=['POST'])
def get_indicator():
    code = request.args.get('code')
    instance = StockDataService()
    indicator = instance.get_indicator(code)
    return jsonify(indicator)

#获取股东人数
@stock_blueprint.route('/stock/getHoderNum', methods=['POST'])
def get_hodernum():
    code = request.args.get('code')
    instance = StockDataService()
    hodernum = instance.get_hodernum(code)
    return jsonify(hodernum)

#获取指数收益(该接口目前失效)
@stock_blueprint.route('/stock/getIndexPerf', methods=['POST'])
def get_index_perf():
    code = request.args.get('code')
    instance = StockDataService()
    index_perf = instance.get_index_perf(code)
    return jsonify(index_perf)





