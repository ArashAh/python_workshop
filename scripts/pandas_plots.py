import pandas as pd
import matplotlib.pyplot as plt
import glob

# Read all CSV files in the current directory
csv_files = glob.glob('*.csv')
dataframes = [pd.read_csv(file) for file in csv_files]

# Concatenate all dataframes
combined_df = pd.concat(dataframes, ignore_index=True)

# Create a line plot
plt.figure(figsize=(10, 6))
combined_df.plot(x='Date', y=['Temperature', 'Humidity'])
plt.title('Temperature and Humidity Over Time')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.savefig('line_plot.png')
#plt.show()

# Create a scatter plot
plt.figure(figsize=(8, 6))
combined_df.plot.scatter(x='Temperature', y='Humidity')
plt.title('Temperature vs Humidity')
plt.xlabel('Temperature')
plt.ylabel('Humidity')
plt.savefig('scatter_plot.png')
#plt.show()

# Create a histogram
plt.figure(figsize=(8, 6))
combined_df['Temperature'].plot.hist(bins=20)
plt.title('Temperature Distribution')
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.savefig('histogram.png')
#plt.show()
