import pandas as pd

# Load the Bowlers_Combined.csv file
file_path = '/Users/siddhantjain/PycharmProjects/NBA Superstars Roles/Files/Bowlers_Combined.csv'
df = pd.read_csv(file_path)

# Round all numerical values to 2 decimal places


# Calculate Total Balls and Total Wickets
df['Total_Balls'] = df['p_balls'] + df['d_balls']
df['Total_Wickets'] = df['p_wickets'] + df['d_wickets']

# Filter out players with 0 wickets
df = df[df['Total_Wickets'] > 0]

# Calculate Strike Rate (Balls per Wicket)
df['Strike Rate'] = df['Total_Balls'] / df['Total_Wickets']

# Calculate league Strike Rate (average across all players)
league_strike_rate = df['Strike Rate'].mean()

# Calculate Strike Rate+
df['Strike Rate+'] = (league_strike_rate / df['Strike Rate']) * 100

# Delete the specified columns (if needed, based on previous code)
columns_to_drop = ['p_runs_bowler','p_Economy','p_Strike Rate','p_Average','p_Economy+','p_Strike Rate+','p_Average+','d_runs_bowler','d_Economy','d_Strike Rate','d_Average','d_Economy+','d_Strike Rate+','d_Average+']
df = df.drop(columns=columns_to_drop, errors='ignore')




# Delete the specified columns (if needed, based on previous code)
columns_to_drop = ['p_runs_bowler','p_Economy','p_Strike Rate','p_Average','p_Economy+','p_Strike Rate+',
                   'p_Average+','d_runs_bowler','d_Economy','d_Strike Rate','d_Average','d_Economy+','d_Strike Rate+','d_Average+',
                   'Wkts','SR','Total_Runs','High Leverage Economy','High Leverage Economy+']
df = df.drop(columns=columns_to_drop, errors='ignore')

# Save the dataframe with the new 'Strike Rate+' column
output_file_path = '/Users/siddhantjain/PycharmProjects/NBA Superstars Roles/Files/Strike_rate+.csv'
df.to_csv(output_file_path, index=False)

df = df.round(2)

print(f"Data with Strike Rate+ saved to: {output_file_path}")