import pandas as pd
data = pd.read_excel('C:\\Users\\khush\\Downloads\\task2.csv')

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(data.head())

# Filter data based on a condition
filtered_data = data[data['feb'] > 4215309]  
print("\nFiltered DataFrame:")
print(filtered_data)

# Handle missing values
data_dropped = data.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(data_dropped)

# Fill missing values with a specified value
data_filled = data.fillna(value={'column_name': 'value_to_fill'})
print("\nDataFrame after filling missing values:")
print(data_filled)

# Calculate summary statistics
summary = data.describe()
print("\nSummary statistics of the DataFrame:")
print(summary)
