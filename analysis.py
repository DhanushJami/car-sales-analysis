import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None

file_path = 'dataset.csv'

try:
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    exit()

print("Dimensions of the dataset:", df.shape)
print("\nFirst few rows of the dataset:")
print(df.head())

print("\nData types of columns:")
print(df.dtypes)

print("\nBasic statistics of the dataset:")
print(df.describe())

df.drop_duplicates(subset=['Price_in_thousands'], keep='first', inplace=True)
df = df[df['sales'] >= 10]
df.fillna(df.mean(numeric_only=True), inplace=True)

price_mean = df['Price_in_thousands'].mean()
print("\nMean for Price_in_thousands:", price_mean)

engine_mode = df['Engine_size'].mode()[0]
print("Mode for Engine_size:", engine_mode)

sales_sum = df['sales'].sum()
print("Sum for sales:", sales_sum)

sales_min = df['sales'].min()
print("Minimum for sales:", sales_min)

sales_max = df['sales'].max()
print("Maximum for sales:", sales_max)

avg_price_by_engine = df.groupby('Engine_size')['Price_in_thousands'].mean()
print("\nAverage Price_in_thousands for each Engine_size:")
print(avg_price_by_engine)

plt.figure(figsize=(16, 12))

plt.subplot(3, 2, 1)
plt.hist(df['Price_in_thousands'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Price_in_thousands')
plt.xlabel('Price_in_thousands')
plt.ylabel('Frequency')
plt.grid(True)

plt.subplot(3, 2, 2)
plt.scatter(df['Engine_size'], df['Price_in_thousands'], color='orange', alpha=0.6)
plt.title('Price vs Engine Size')
plt.xlabel('Engine Size')
plt.ylabel('Price in Thousands')
plt.grid(True)

price_ranges = [(10, 20), (20, 30), (30, 40)]
price_counts = [((df['Price_in_thousands'] >= low) & (df['Price_in_thousands'] < high)).sum()
                for low, high in price_ranges]
labels = [f'{low}-{high}' for low, high in price_ranges]

plt.subplot(3, 2, 3)
plt.pie(price_counts, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Price Range Distribution')
plt.legend(labels, loc="best")

plt.subplot(3, 2, 4)
plt.plot(df['Horsepower'], color='green')
plt.title('Horsepower over Index')
plt.xlabel('Index')
plt.ylabel('Horsepower')
plt.grid(True)

plt.subplot(3, 2, 5)
fuel_efficiency_grouped = df.groupby('Fuel_efficiency')['Engine_size'].mean()
fuel_efficiency_grouped.plot(kind='bar', color='salmon')
plt.title('Avg Engine Size by Fuel Efficiency')
plt.xlabel('Fuel Efficiency')
plt.ylabel('Average Engine Size')
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()
