import json
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense


def predict(formatted_name):
    vegetable_name = formatted_name.replace('-', ' ')
    json_file_path = "30_days.json"
    with open(json_file_path, "r") as file:
        da = json.load(file)

    market_prices = da.get(vegetable_name, [])
    if market_prices:
        market_prices_int = [int(price) for price in market_prices]
        print("Market Prices:", market_prices_int)
    else:
        print("Vegetable not found in the data.")

    data = market_prices_int
    sequence_length = 25

    X = []
    y = []

    for i in range(len(data) - sequence_length):
        X.append(data[i:i + sequence_length])
        y.append(data[i + sequence_length])

    X = np.array(X)
    y = np.array(y)

    print(X.shape)

    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(sequence_length, 1)))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mean_squared_error')

    model.fit(X, y, epochs=100, batch_size=1)

    last_sequence = data[-sequence_length:]
    last_sequence = np.array(last_sequence).reshape(1, sequence_length, 1)
    predicted_price = model.predict(last_sequence)
    return str(predicted_price[0][0])


def getPrice(formatted_name):
    print(formatted_name)
    vegetable_name = formatted_name.replace('-', ' ')
    json_file_path = "30_days.json"
    with open(json_file_path, "r") as file:
        da = json.load(file)

    market_prices = da.get(vegetable_name, [])
    if market_prices:
        market_prices_int = [int(price) for price in market_prices]
        return market_prices_int
    else:
        return "Data Not Found"
