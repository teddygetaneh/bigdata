<<<<<<< HEAD
import pandas as pd
from scipy import stats

# Define the path to the CSV file (or Parquet file if you're using that format)
file_path = "cleaned_amazon_data.csv"  # Update the path accordingly

# Load the dataset into a pandas DataFrame
try:
    df = pd.read_csv(file_path)  # Use pd.read_parquet(file_path) for Parquet files
    print("Dataset loaded successfully!")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Data Cleaning
# Remove rows with missing critical values (e.g., title, price)
df = df.dropna(subset=['title', 'price'])

# Fill missing 'stars' values with the mean of the column
df['stars'] = df['stars'].fillna(df['stars'].mean())

# Remove duplicate rows based on 'asin' (Amazon Standard Identification Number)
df = df.drop_duplicates(subset=['asin'])

# Convert 'price' column to numeric (handling errors by coercing invalid values)
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Feature Engineering
# Define price bins
bins = [0, 50, 200, 1000, float('inf')]
labels = ['Low', 'Medium', 'High', 'Premium']
df['price_category'] = pd.cut(df['price'], bins=bins, labels=labels)

# Data Aggregation (example: calculate average rating by asin)
df_product_avg_rating = df.groupby('asin')['stars'].mean().reset_index()

# Handling Outliers (Using Z-score to identify outliers in 'price')
z_scores = stats.zscore(df['price'].dropna())
df = df[(z_scores < 3) & (z_scores > -3)]  # Remove outliers beyond 3 standard deviations

# Final Data Check
print("\nMissing Values after Transformation:")
print(df.isnull().sum())

print("\nData Types after Transformation:")
print(df.dtypes)

print("\nFirst few rows after Transformation:")
print(df.head())

# Save the Transformed Data
df.to_csv('transformed_amazon_data.csv', index=False)
print("Transformed data saved as 'transformed_amazon_data.csv'.")
=======
import pandas as pd
from scipy import stats

# Define the path to the CSV file (or Parquet file if you're using that format)
file_path = "cleaned_amazon_data.csv"  # Update the path accordingly

# Load the dataset into a pandas DataFrame
try:
    df = pd.read_csv(file_path)  # Use pd.read_parquet(file_path) for Parquet files
    print("Dataset loaded successfully!")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Data Cleaning
# Remove rows with missing critical values (e.g., title, price)
df = df.dropna(subset=['title', 'price'])

# Fill missing 'stars' values with the mean of the column
df['stars'] = df['stars'].fillna(df['stars'].mean())

# Remove duplicate rows based on 'asin' (Amazon Standard Identification Number)
df = df.drop_duplicates(subset=['asin'])

# Convert 'price' column to numeric (handling errors by coercing invalid values)
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Feature Engineering
# Define price bins
bins = [0, 50, 200, 1000, float('inf')]
labels = ['Low', 'Medium', 'High', 'Premium']
df['price_category'] = pd.cut(df['price'], bins=bins, labels=labels)

# Data Aggregation (example: calculate average rating by asin)
df_product_avg_rating = df.groupby('asin')['stars'].mean().reset_index()

# Handling Outliers (Using Z-score to identify outliers in 'price')
z_scores = stats.zscore(df['price'].dropna())
df = df[(z_scores < 3) & (z_scores > -3)]  # Remove outliers beyond 3 standard deviations

# Final Data Check
print("\nMissing Values after Transformation:")
print(df.isnull().sum())

print("\nData Types after Transformation:")
print(df.dtypes)

print("\nFirst few rows after Transformation:")
print(df.head())

# Save the Transformed Data
df.to_csv('transformed_amazon_data.csv', index=False)
print("Transformed data saved as 'transformed_amazon_data.csv'.")
>>>>>>> 0d1c825 (Initial commit)
