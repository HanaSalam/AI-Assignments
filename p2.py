"""
Day15
2. Develop a model to do classification in the sonar.csv dataset.
"""
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from sklearn.datasets import load_iris
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.read_csv('sonar.csv')
data=data.as_matrix()
X = data[:,0:60]
y = data[:,-1]

encoder = LabelEncoder()
y = encoder.transform(y).reshape(-1,1)
enc = OneHotEncoder()
y=encoder.fit_transform(y) #one hot--1st fit and then transform
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
model = Sequential()
model.add(Dense(10,input_shape=(60,),activation='relu'))
model.add(Dense(10,activation='relu'))
model.add(Dense(2,activation='softmax'))
optimizer=Adam(lr=0.001)
print model.summary()
model.compile(optimizer,loss='categorical_crossentropy',metrics=['accuracy'])
model.fit(X_train,y_train,batch_size=5,verbose=2,epochs=100)
results = model.evaluate(X_test,y_test)

print(results[0]) #loss
print(results[1]) #accuracy
