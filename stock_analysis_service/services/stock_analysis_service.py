from stock_analysis_service.dao.stock_analysis_dao import StockAnalysisDao
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.optimizers import RMSprop
import json
import matplotlib.pyplot as plt
import matplotlib

from sklearn.metrics import mean_squared_error
from math import sqrt


class StockAnalysisService:
    def __init__(self):
        self.dao = StockAnalysisDao()

    def plot_results(self, y_true, y_pred, title="StockPridiction", filename="stock_prediction.png"):
        plt.figure(figsize=(10, 5))
        plt.plot(y_true, label='Acutal')
        plt.plot(y_pred, label='Prediction', linestyle='--')
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.title(title)
        plt.legend()
        plt.savefig(filename)
        plt.close()

    def LSTM(self, code):

        # 返回的是df数据
        data=self.dao.get_kline(code)
        data_lstm = data[['timestamp', 'volume', 'open', 'high', 'low', 'close', 'chg', 'turnoverrate']]

        # 对数据进行归一化处理
        scaler = MinMaxScaler()
        data_scaled = scaler.fit_transform(data_lstm.drop('timestamp', axis=1))

        def create_dataset(data, look_back=1):
            X, Y = [], []
            for i in range(len(data) - look_back):
                X.append(data[i:(i + look_back), :])
                Y.append(data[i + look_back, [2, 3, 4]])  # -2是收盘价所在的列
            return np.array(X), np.array(Y)

        look_back = 5
        X, Y = create_dataset(data_scaled, look_back)

        # 划分训练集和测试集
        train_size = int(len(X) * 0.8)
        X_train, X_test = X[:train_size], X[train_size:]
        Y_train, Y_test = Y[:train_size], Y[train_size:]

        # 创建和训练LSTM模型：
        model = Sequential()
        model.add(LSTM(64, input_shape=(look_back, X_train.shape[2])))

        model.add(Dense(3))
        model.compile(optimizer=RMSprop(learning_rate=0.003), loss='mse')
        model.fit(X_train, Y_train, epochs=100, batch_size=32, verbose=0)

        def predict_next_n_days(model, data, n_days, look_back):
            predictions = []
            input_data = data[-look_back:].copy()

            for _ in range(n_days):
                input_array = np.array([input_data[-look_back:]])
                predicted_value = model.predict(input_array)
                predictions.append(predicted_value[0][:3])
                new_row = input_data[-1].copy()  # 创建新行并复制前一天的值
                new_row[[2, 3, 4]] = predicted_value
                input_data = np.vstack((input_data, new_row))  # 添加预测值并保持维度一致

            return predictions

        predicted_closes_scaled = predict_next_n_days(model, data_scaled, 5, look_back)
        # 创建一个形状匹配的零数组，并将预测值插入最后一列
        # 获取收盘价的缩放参数
        close_scaler = MinMaxScaler()
        close_scaler.min_, close_scaler.scale_ = scaler.min_[4], scaler.scale_[4]

        predicted_array = np.zeros((len(predicted_closes_scaled), 3))
        predicted_array[:, :] = np.array(predicted_closes_scaled)

        # 使用收盘价的缩放参数进行反向缩放
        full_predicted_array = np.zeros((len(predicted_closes_scaled), data_scaled.shape[1]))
        full_predicted_array[:, [2, 3, 4]] = predicted_array
        predicted_prices = scaler.inverse_transform(full_predicted_array)[:, [2, 3, 4]]


        print("预测未来5天的最高价、最低价和收盘价：")
        for i, prices in enumerate(predicted_prices):
            print(f"Day {i + 1}: High - {prices[0]:.2f}, Low - {prices[1]:.2f}, Close - {prices[2]:.2f}")

        # 计算预测值
        Y_pred = model.predict(X_test)

        # 准备一个与Y_pred形状匹配的零数组，插入预测值到正确的列中
        predicted_array = np.zeros((Y_pred.shape[0], data_scaled.shape[1]))
        predicted_array[:, [2, 3, 4]] = Y_pred

        # 对预测值进行反向缩放
        Y_pred_prices = scaler.inverse_transform(predicted_array)[:, [2, 3, 4]]

        # 准备一个与Y_test形状匹配的零数组，插入实际值到正确的列中
        true_array = np.zeros((Y_test.shape[0], data_scaled.shape[1]))
        true_array[:, [2, 3, 4]] = Y_test

        # 对实际值进行反向缩放
        Y_true_prices = scaler.inverse_transform(true_array)[:, [2, 3, 4]]

        # 绘制预测值和实际值的对比图表
        self.plot_results(Y_true_prices[:, 2], Y_pred_prices[:, 2], title="StockPridiction", filename="stock_prediction.png")

        return json.dumps(predicted_prices.tolist())

