<<<<<<< HEAD
import pandas as pd

# Define the path to the CSV file (or Parquet file if you're using that format)
file_path = "amazon_products.csv"  # Update the path accordingly

# Load the dataset into a pandas DataFrame
try:
    df = pd.read_csv(file_path)  # Use pd.read_parquet(file_path) for Parquet files
    print("Dataset loaded successfully!")
except Exception as e:
    print(f"Error loading dataset: {e}")

# 1.3. Explore the Dataset

# Check the DataFrame's shape (number of rows and columns)
print("DataFrame Shape:", df.shape)

# View the columns and their data types
print("\nDataFrame Info:")
print(df.info())

# Examine the first few rows to check the data
print("\nFirst few rows of the dataset:")
print(df.head())

# Get basic statistics for numeric columns (e.g., price, rating, etc.)
print("\nBasic Statistics:")
print(df.describe())

# List all column names to ensure the dataset contains the relevant columns
print("\nColumn Names:")
print(df.columns)

# 1.4. Handle Missing Values and Duplicates

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check for duplicates
print("\nDuplicates:")
print(df.duplicated().sum())

# 1.5. Initial Data Cleaning (Optional)

# Remove rows with missing critical values (e.g., product_name, price)
df = df.dropna(subset=['title', 'price'])

# Fill missing values for non-essential columns (e.g., rating)
df['stars'] = df['stars'].fillna(df['stars'].mean())

# Remove duplicate rows based on specific columns (e.g., product_id)
df = df.drop_duplicates(subset=['asin'])

# Convert columns to appropriate data types (e.g., converting price to numeric)
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# 1.6. Save the Cleaned Data (Optional)

# Save as CSV
df.to_csv('cleaned_amazon_data.csv', index=False)
print("\nCleaned data saved as 'cleaned_amazon_data.csv'.")

=======
import pandas as pd

# Define the path to the CSV file (or Parquet file if you're using that format)
file_path = "amazon_products.csv"  # Update the path accordingly

# Load the dataset into a pandas DataFrame
try:
    df = pd.read_csv(file_path)  # Use pd.read_parquet(file_path) for Parquet files
    print("Dataset loaded successfully!")
except Exception as e:
    print(f"Error loading dataset: {e}")

# 1.3. Explore the Dataset

# Check the DataFrame's shape (number of rows and columns)
print("DataFrame Shape:", df.shape)

# View the columns and their data types
print("\nDataFrame Info:")
print(df.info())

# Examine the first few rows to check the data
print("\nFirst few rows of the dataset:")
print(df.head())

# Get basic statistics for numeric columns (e.g., price, rating, etc.)
print("\nBasic Statistics:")
print(df.describe())

# List all column names to ensure the dataset contains the relevant columns
print("\nColumn Names:")
print(df.columns)

# 1.4. Handle Missing Values and Duplicates

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check for duplicates
print("\nDuplicates:")
print(df.duplicated().sum())

# 1.5. Initial Data Cleaning (Optional)

# Remove rows with missing critical values (e.g., product_name, price)
df = df.dropna(subset=['title', 'price'])

# Fill missing values for non-essential columns (e.g., rating)
df['stars'] = df['stars'].fillna(df['stars'].mean())

# Remove duplicate rows based on specific columns (e.g., product_id)
df = df.drop_duplicates(subset=['asin'])

# Convert columns to appropriate data types (e.g., converting price to numeric)
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# 1.6. Save the Cleaned Data (Optional)

# Save as CSV
df.to_csv('cleaned_amazon_data.csv', index=False)
print("\nCleaned data saved as 'cleaned_amazon_data.csv'.")

>>>>>>> 0d1c825 (Initial commit)
