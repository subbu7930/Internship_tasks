import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales_data.csv")

print("Dataset Overview")
print(df.head)
print("\nSummary Statistics: ")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())

df['Date'] = pd.to_datetime(df['Date'])
df = df.dropna()

# Sales by Region
plt.figure(figsize=(8, 5))
sns.barplot(x="Region", y="Sales", data = df)
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(x="Product", y="Profit", data=df)
plt.title("Profit by Product")
plt.xlabel("Product")
plt.ylabel("Profit")
plt.show()

plt.figure(figsize=(7, 5))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()