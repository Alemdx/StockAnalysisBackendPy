import pysnowball as ball
import json
from flask import Blueprint, jsonify, request
from pymongo import MongoClient








    # xqat = 80
    # f8d831418bba697ce50569d95b51cbd92d8926;

if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017/')
    db = client['StockAnalysisMongo']  # 替换为你的数据库名
    collection = db['StockHistory']  # 替换为你的集合名
    ball.set_token('xq_a_token = ad05a37d39333d61ecfec920560cc1bad41bed96')
    collection.insert_one(ball.quote_detail("SH600161"))
    # print(type(ball.index_perf_90("399967")))








