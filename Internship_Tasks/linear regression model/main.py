import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("house_data.csv")

print("\nDataset Loaded Successfully!")
print(df.head())

df = df.fillna(0)
print("\nAfter Filling Missing Values:", df.shape)

features = ["LotArea", "BedroomAbvGr", "GrLivArea", "Neighborhood"]
target = "SalePrice"

X = df[features]
y = df[target]

column_transformers = ColumnTransformer(
    transformers=[
        ("encoder", OneHotEncoder(), ["Neighborhood"])
    ],
    remainder='passthrough'
)

X = column_transformers.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\Data Split Successfully")

model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel Training Completed")

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation")
print("Mean Squared Error (MSE):", mse)
print("R2 Score:", r2)

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual House Price")
plt.ylabel("Predicted House Price")
plt.title("Actual vs Predicyed House Price")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(df["SalePrice"], kde=True)
plt.title("Distribution of House Prices")
plt.show()