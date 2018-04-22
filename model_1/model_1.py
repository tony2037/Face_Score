#!/usr/bin/env python3  
from keras.datasets import mnist  
from keras.utils import np_utils  
from keras.models import Sequential  
from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D  
import numpy as np  
import data
np.random.seed(10)  
  

# Read image data  
(X_Train, y_Train), (X_Test, y_Test) = data.load_data(x_path="./dataset/x/", y_path="./dataset/y/")  
  
"""
# Translation of data  
X_Train40 = X_Train.reshape(X_Train.shape[0], 28, 28, 1).astype('float32')  
X_Test40 = X_Test.reshape(X_Test.shape[0], 28, 28, 1).astype('float32')  
"""
print("X_Train shape : {}".format(X_Train.shape))
print("y_Train shape : {}".format(y_Train.shape))

# define image size (h,w,c)
image_size = (256,256,3)
# Create model  
model = Sequential()  
# Create CN layer 1  
model.add(Conv2D(filters=16,  
                 kernel_size=(5,5),  
                 padding='same',  
                 input_shape=image_size,  
                 activation='relu'))  
# Create Max-Pool 1  
model.add(MaxPooling2D(pool_size=(2,2)))  
  
# Create CN layer 2  
model.add(Conv2D(filters=36,  
                 kernel_size=(5,5),  
                 padding='same',  
                 input_shape=image_size,  
                 activation='relu'))  
  
# Create Max-Pool 2  
model.add(MaxPooling2D(pool_size=(2,2)))  
  
# Add Dropout layer  
#model.add(Dropout(0.25))  
# Add flatten layer
model.add(Flatten())  

model.add(Dense(128, activation='relu'))
# Add Dropout layer   
#model.add(Dropout(0.5))

model.add(Dense(1, activation='relu'))  

model.summary()  
print("") 

# 定義訓練方式  
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])  
  
# 開始訓練  
train_history = model.fit(x=X_Train,  
                          y=y_Train, validation_split=0.2,  
                          epochs=10, batch_size=1, verbose=2)
