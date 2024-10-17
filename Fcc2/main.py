import pandas as pd
from demographic_data_analyzer import demographic_data_analyzer

# Load your dataset
df = pd.read_csv('demographic_data.csv')  # Ensure this file exists

# Analyze the demographic data
results = demographic_data_analyzer(df)

# Print the results
for key, value in results.items():
    print(f"{key}: {value}")
