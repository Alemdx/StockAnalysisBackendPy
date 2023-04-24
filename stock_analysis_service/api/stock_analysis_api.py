from flask import Blueprint, jsonify, request
from stock_analysis_service.services.stock_analysis_service import StockAnalysisService

service_blueprint = Blueprint('service', __name__)

# 获取股票详情
@service_blueprint.route('/service/LSTM', methods=['POST'])
def LSTM():
    code = request.args.get('code')
    instance = StockAnalysisService()
    detail = instance.LSTM(code)
    return jsonify(detail)
