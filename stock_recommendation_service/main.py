from flask import Flask
from flask_cors import CORS
from stock_recommendation_service.api.stock_recommendation_api import recommendation_blueprint
import py_eureka_client.eureka_client as eureka_client

app = Flask(__name__)
app.register_blueprint(recommendation_blueprint)
CORS(app)

if __name__ == '__main__':
    # dataservice的所有服务
    app.run(
        port=5002,
    )