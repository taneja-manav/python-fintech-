import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv("Linear-Regression-_Training-Data_-.csv")
print(data.head())

# Independent variable(x)
x = data[["Age","Education","Income","Vehicle Ownership"]]

# Dependent variable(y)
y = data[["Purchase hybrid vehicle"]]

# train test split(80:20)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=56)

# train the model

model=LinearRegression()
model.fit(x_train,y_train)

# predict on test data 

y_pred=model.predict(x_test)

# evaluate the mode
print("Mean Squared Error:",mean_squared_error(y_test,y_pred))

# load new data
new_data=pd.read_csv("Linear-Regression-Python-_Test-data_.csv")
print(new_data.head())

new_data["prediction percentage"]=np.round(model.predict(new_data)*100,2)
print(new_data.head(10))

new_data.to_csv("Car Purchase Prediction.csv",index=False)