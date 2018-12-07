"""1. Develop a model to do iris classification problem using Keras
Sequential model. Run the model for varying number of epochs
and batch sizes and observe the accuracy
"""

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from sklearn.datasets import load_iris
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
iris = load_iris()
X=iris.data
y=iris.target.reshape(-1,1)
print y
encoder = OneHotEncoder()
y=encoder.fit_transform(y)
#print y
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
model = Sequential()
model.add(Dense(4,input_shape=(4,),activation='tanh'))
model.add(Dense(10,activation='relu'))
model.add(Dense(3,activation='softmax'))
optimizer = Adam(lr = 0.001)
print model.summary()
model.compile(optimizer,loss='categorical_crossentropy',metrics=['accuracy'])
model.fit(X_train,y_train,verbose=2,epochs=100)
results = model.evaluate(X_test,y_test)
print(results[0]) #loss
print(results[1]) #accuracy
