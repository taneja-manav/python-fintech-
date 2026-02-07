import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("House_Price_Training_Data.csv")


x=data.drop("Price_Lakhs",axis=1)
y=data[["Price_Lakhs"]]

categorical_cols=["Furnishing_Status","Locality_Category"]


data_split = pd.get_dummies(x,columns=categorical_cols)
print(data_split.head())

x_train,x_test,y_train,y_test=train_test_split(data_split,y,test_size=0.2,random_state=42)

scaler=StandardScaler()
x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.fit_transform(x_test)

model=LinearRegression()
model.fit(x_train_scaled,y_train)

y_pred=model.predict(x_test_scaled)


print("Mean Squared Error:",mean_squared_error(y_test,y_pred))

new_data=pd.read_csv("House_Price_NewData.csv")

new_data_encoded = pd.get_dummies(new_data,columns=categorical_cols)

new_data_scaled=scaler.transform(new_data_encoded)

new_data["Price_Lakhs"]=np.round(model.predict(new_data_scaled),2)
print(new_data.head(10))



