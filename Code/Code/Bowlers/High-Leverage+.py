import pandas as pd

# Load the Bowlers_Combined.csv file
file_path = '/Users/siddhantjain/PycharmProjects/NBA Superstars Roles/Files/Bowlers_Combined.csv'
df = pd.read_csv(file_path)

# Round all numerical values to 2 decimal places
df = df.round(2)

# Calculate High Leverage Economy
df['Total_Balls'] = df['p_balls'] + df['d_balls']
df['Total_Runs'] = df['p_runs_bowler'] + df['d_runs_bowler']
df['High Leverage Economy'] = (df['Total_Runs'] / df['Total_Balls']) * 6


# Calculate league High Leverage Economy (average across all players)
league_high_leverage_economy = df['High Leverage Economy'].mean()

# Calculate High Leverage Economy+
df['High Leverage Economy+'] = (league_high_leverage_economy / df['High Leverage Economy']) * 100

# Delete the specified columns
columns_to_drop = ['Mat', 'Inns', 'Ov', 'Runs', 'BBI', 'Avg', 'Econ', 'Sr', '4w', '5w', 'Sold', 'Player_auction']
df = df.drop(columns=columns_to_drop, errors='ignore')

# Save the updated dataframe back to a new CSV file
output_file_path = '/Users/siddhantjain/PycharmProjects/NBA Superstars Roles/Files/Bowlers_Combined.csv'
df.to_csv(output_file_path, index=False)

print(f"Updated file with High Leverage Economy+ saved to: {output_file_path}")
