import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Week': ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6'],
    'Visitors': [120, 130, 125, 140, 135, 150],
    'Conversions': [30, 40, 35, 45, 50, 55]
}

df = pd.DataFrame(data)

# Bar Chart
plt.figure(figsize=(10, 5))
plt.bar(df['Week'], df['Visitors'], color='orange', label='Visitors')
plt.xlabel('Week')
plt.ylabel('Number of Visitors')
plt.title('Weekly Visitors')
plt.legend()
plt.show()

# Line Chart
plt.figure(figsize=(10, 5))
plt.plot(df['Week'], df['Visitors'], marker='o', color='orange', label='Visitors')
plt.plot(df['Week'], df['Conversions'], marker='s', color='blue', label='Conversions')
plt.xlabel('Week')
plt.ylabel('Number')
plt.title('Weekly Visitors and Conversions')
plt.legend()
plt.show()
