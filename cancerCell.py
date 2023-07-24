import pandas as pd

dataset=pd.read_csv('cancer.csv')

x=dataset.drop(columns=["diagnosis(1=m, 0=b)"])
y=dataset["diagnosis(1=m, 0=b)"]

from sklearn.model_selection import train_test_split
x_test,x_train,y_test,y_train = train_test_split(x,y,test_size=0.2)

import tensorflow as tf
import tensorflow as tf

# Assuming x_train contains the training data with shape (num_samples, num_features)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(256, input_shape=x_train.shape[1:], activation='sigmoid'))

model.add(tf.keras.layers.Dense(256,activation='sigmoid'))
model.add(tf.keras.layers.Dense(1,activation='sigmoid'))

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
model.fit(x_train, y_train, epochs=100)