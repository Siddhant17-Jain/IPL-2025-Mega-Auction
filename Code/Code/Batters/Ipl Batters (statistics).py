import pandas as pd

# Load the CSV file
file_path = '/Files/Old Files/IPL Batters.csv'
df = pd.read_csv(file_path)

# Convert Avg and SR to numeric, forcing invalid entries (like '-') to NaN
df['Avg'] = pd.to_numeric(df['Avg'], errors='coerce')
df['SR'] = pd.to_numeric(df['SR'], errors='coerce')

# Drop rows where Avg or SR is NaN
df = df.dropna(subset=['Avg', 'SR'])

# Create the BASRA column
df['BASRA'] = df['Avg'] + df['SR']

# Calculate league averages for Avg, SR, and BASRA
league_avg_avg = df['Avg'].mean()
league_avg_sr = df['SR'].mean()
league_avg_basra = df['BASRA'].mean()

# Normalize the columns such that 100 is league average (like ERA+ calculation)
df['Avg+ (100 scale)'] = (df['Avg'] / league_avg_avg) * 100
df['SR+ (100 scale)'] = (df['SR'] / league_avg_sr) * 100
df['BASRA+ (100 scale)'] = (df['BASRA'] / league_avg_basra) * 100

# Round the relevant columns to 2 decimal places
df['Avg+ (100 scale)'] = df['Avg+ (100 scale)'].round(2)
df['SR+ (100 scale)'] = df['SR+ (100 scale)'].round(2)
df['BASRA+ (100 scale)'] = df['BASRA+ (100 scale)'].round(2)

# Save the updated DataFrame back to a CSV file
df.to_csv('/Users/siddhantjain/PycharmProjects/NBA Superstars Roles/Files/IPL_Batters_Updated.csv', index=False)

print("File updated with BASRA and regressed columns (rounded to 2 decimal places). Saved as 'IPL_Batters_Updated.csv'")
