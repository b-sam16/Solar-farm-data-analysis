import pandas as pd

# Load the datasets
benin = pd.read_csv('./data/benin-malanville.csv')
sierra_leone = pd.read_csv('./data/sierraleone-bumbuna.csv')
togo = pd.read_csv('./data/togo-dapaong_qc.csv')

# Add a "Country" column
benin['Country'] = 'Benin'
sierra_leone['Country'] = 'Sierra Leone'
togo['Country'] = 'Togo'

# Combine all datasets
combined_data = pd.concat([benin, sierra_leone, togo], ignore_index=True)

# Save the combined dataset to a new CSV file
combined_data.to_csv('./data/combined_solar_data.csv', index=False)

print("Data successfully combined and saved as 'combined_solar_data.csv'.")