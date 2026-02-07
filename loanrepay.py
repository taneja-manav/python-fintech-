import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv("Loan_Repayment_Training_Data.csv")

# define x and y

x=data.drop("Repayment Probability", axis=1)
y=data[["Repayment Probability"]]    

categorical_cols = ["Employment Status","Marital Status","Education Level"]

x=pd.get_dummies(x,columns=categorical_cols)
print(x.head())


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

print(y_pred)

print("Mean Squared Error:",mean_squared_error(y_test,y_pred))


# Load new data 

new_data = pd.read_csv("Loan_Repayment_Test_Data_NoLabel.csv")
new_data_encoded=pd.get_dummies(new_data,columns=categorical_cols)

print(new_data.head())


new_data["Repayment Probability"]=np.round(model.predict(new_data_encoded),2)
print(new_data.head(10))

new_data.to_csv("repayment_prediction.csv",index=False)