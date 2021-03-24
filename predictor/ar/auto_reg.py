import requests
import pandas as pd
from statsmodels.tsa.ar_model import AutoReg
import numpy as np
from sklearn.metrics import mean_squared_error


r = requests.get('http://localhost:8000/inputdata/?device=1')
data = r.json()

df = pd.DataFrame(data)

df['datetime'] = pd.to_datetime(df['datetime'])

df_predict = df[['value', 'datetime']]

print(df_predict.shape[0])

df_predict.set_index('datetime', inplace=True)

df.set_index('datetime', inplace=True)

lista = np.linspace(1,25,25)

split_value = int(round(df_predict.index.size * 0.3))

df_train = df_predict[:df_predict.index.size - split_value]

df_test = df_predict[-split_value:]

model = AutoReg(df_train.values, lags=lista, trend='c', seasonal=True, period=35, old_names=False).fit()

prediction = model.predict(start=df_predict.shape[0] - df_test.shape[0], end=df_predict.shape[0] - 1)

score = mean_squared_error(df_test['value'], prediction)

print(f'score: {score}')