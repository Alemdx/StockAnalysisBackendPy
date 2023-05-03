from flask import Blueprint, jsonify, request
from stock_recommendation_service.services.stock_recommendation_service import StockRecommendationService

recommendation_blueprint = Blueprint('recommendation', __name__)

# 获取股票详情
@recommendation_blueprint.route('/recommendation/getNewHighIndex', methods=['POST'])
def getNewHighIndex():
    code = request.args.get('code')
    print(code)
    day=request.args.get('day')
    instance = StockRecommendationService()
    if(instance.has_new_high(code,day)):
        return "yes"
    else:
        return "no"

@recommendation_blueprint.route('/recommendation/getBioStock', methods=['GET'])
def getBioStock():
    instance=StockRecommendationService();
    return str(instance.get_bio_stock())

@recommendation_blueprint.route('/recommendation/getConStock', methods=['GET'])
def getConStock():
    instance=StockRecommendationService();
    return str(instance.get_con_stock())

