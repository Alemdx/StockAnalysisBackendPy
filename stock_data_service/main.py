from flask import Flask
from flask_cors import CORS
from stock_data_service.api.stock_data_api import stock_blueprint
import py_eureka_client.eureka_client as eureka_client

app = Flask(__name__)
app.register_blueprint(stock_blueprint)
CORS(app)

# 将dataservice注册到eureka中
def setEureka():
    server_host = "localhost"
    server_port = 5000
    eureka_client.init(eureka_server="http://localhost:2001/eureka",
                       app_name="Stock-Data-Service",
                       # 当前组件的主机名，可选参数，如果不填写会自动计算一个，如果服务和 eureka 服务器部署在同一台机器，请必须填写，否则会计算出 127.0.0.1
                       instance_host=server_host,
                       instance_port=server_port,
                       # 调用其他服务时的高可用策略，可选，默认为随机
                       ha_strategy=eureka_client.HA_STRATEGY_RANDOM)

setEureka()
if __name__ == '__main__':
    # dataservice的所有服务
    app.run()
