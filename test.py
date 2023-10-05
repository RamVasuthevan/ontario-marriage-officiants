# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('registered_marriage_officiants.csv')

# Set the maximum column width for the "Affiliation" column
pd.set_option('display.max_colwidth', 100)

# Display basic data statistics
data_summary = df.describe()

# Count unique municipalities and affiliations
unique_municipalities = df['Municipality'].nunique()
unique_affiliations = df['Affiliation'].nunique()

# Visualize the distribution of officiants by municipality
municipality_counts = df['Municipality'].value_counts()

# Visualize the distribution of affiliations
affiliation_counts = df['Affiliation'].value_counts().head(10)

# Plot the data
plt.figure(figsize=(12, 6))

# Plot 1: Distribution of officiants by municipality
plt.subplot(1, 2, 1)
municipality_counts.plot(kind='bar', title='Distribution of Officiants by Municipality')
plt.xlabel('Municipality')
plt.ylabel('Number of Officiants')

# Plot 2: Top 10 Affiliations
plt.subplot(1, 2, 2)
affiliation_counts.plot(kind='bar', title='Top 10 Affiliations')
plt.xlabel('Affiliation')
plt.ylabel('Number of Officiants')

plt.tight_layout()
plt.show()

# Display the data summary and unique counts
print("Data Summary:")
print(data_summary)
print(f"Unique Municipalities: {unique_municipalities}")
print(f"Unique Affiliations: {unique_affiliations}")