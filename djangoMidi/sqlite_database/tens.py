import numpy as np
import pandas as pd
import random
from tensorflow.keras.models import Sequential
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.python.keras.utils import np_utils
import database_tool as d_t

'''
df = d_t.translate_sqldb_to_dataframe('project_database.db', 'trans_list')
data=df[['height','weight','target','wpd/step','jpd/km']]
data=data.iloc[0:]
data=data.dropna()
'''

def tens_model_jpd(user_input_data):
 df = d_t.translate_sqldb_to_dataframe('project_database.db', 'trans_list')
 data=df[['height','weight','target','wpd/step','jpd/km']]
 data=data.iloc[0:]
 #data=data.dropna()
 
 x_train = data[['height','weight','target']].iloc[1:40]
 y_train = data[['jpd/km']].iloc[1:40]


 x_train = x_train.to_numpy()
 y_train = y_train.to_numpy()
 

 model = Sequential()
 #建立神經網路第一層，1個神經元，輸入為1個數值
 model.add(Dense(units=30, input_shape=(3,), activation = 'linear'))
 model.add(Dense(units=30, input_shape=(3,), activation = 'linear'))
 model.add(Dense(units=30, input_shape=(3,), activation = 'linear'))
 model.add(Dense(units=1, input_shape=(3,), activation = 'linear'))


 #訓練神經網路，使用何種loss function, 何種gradient descent
 model.compile(loss='mse', optimizer='adam', metrics=['mape'])
 
 train_history = model.fit(x=x_train,y=y_train,epochs=1000,batch_size=500)

 #預測
 user_input_data = user_input_data[['height','weight','target']].to_numpy()
 predictions = model.predict(user_input_data)
 #轉換成整數(由np格式轉換)
 predictions = np.array(predictions, dtype='i') 
 return predictions


def tens_model_wpd(user_input_data):
 df = d_t.translate_sqldb_to_dataframe('project_database.db', 'trans_list')
 data=df[['height','weight','target','wpd/step','jpd/km']]
 data=data.iloc[0:]
 #data=data.dropna()
 x_train = data[['height','weight','target']].iloc[1:40]
 y_train = data[['wpd/step']].iloc[1:40]



 x_train = x_train.to_numpy()
 y_train = y_train.to_numpy()

 model = Sequential()
 #建立神經網路第一層，1個神經元，輸入為1個數值
 model.add(Dense(units=30, input_shape=(3,), activation = 'linear'))
 model.add(Dense(units=30, input_shape=(3,), activation = 'linear'))
 model.add(Dense(units=30, input_shape=(3,), activation = 'linear'))
 model.add(Dense(units=1, input_shape=(3,), activation = 'linear'))


 #訓練神經網路，使用何種loss function, 何種gradient descent
 model.compile(loss='mse', optimizer='adam', metrics=['mape'])

 train_history = model.fit(x=x_train,y=y_train,epochs=1000,batch_size=500)

 #預測
 user_input_data = user_input_data[['height','weight','target']].to_numpy()
 predictions = model.predict(user_input_data)
 #轉換成整數(由np格式轉換)
 predictions = np.array(predictions, dtype='i') 
 return predictions


data2 = 'e'
def meal(data2):
 list_n = [1,3,4,5,9,11,12,14,15]
 list_p = [2,6,7,8,10,13]
 list_e = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
 if data2 == 'n':
    status_n = random.choice(list_n)    
    return status_n     

 if data2 == 'p':
    status_p = random.choice(list_p)
    return status_p

 if data2 == 'e':
    status_e = random.choice(list_e)
    return status_e

