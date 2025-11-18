import pandas as pd
import matplotlib.pyplot as plt

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

# List of players to highlight
highlight_players = ['Arshdeep Singh', 'Trent Boult', 'Mohammad Siraj', 'Mitchell Starc']

# Create a column to flag if the player is one of the highlighted players
df['highlight'] = df['Player'].apply(lambda x: x in highlight_players)

# Plot: High Leverage Economy+ vs Winning Bid
plt.figure(figsize=(14, 7))
plt.scatter(df['High Leverage Economy+'], df['Winning_Bid'], c=df['highlight'].map({True: 'red', False: 'blue'}), alpha=0.6)

# Highlight the players specifically and add their names (bolded) on the plot
for player in highlight_players:
    # Check if the player exists in the dataframe
    player_data = df[df['Player'] == player]
    if not player_data.empty:
        plt.scatter(player_data['High Leverage Economy+'], player_data['Winning_Bid'], s=100, edgecolor='black', zorder=5)
        plt.text(player_data['High Leverage Economy+'].values[0], player_data['Winning_Bid'].values[0],
                 f"{player}", fontsize=9, ha='right', va='bottom', color='black', fontweight='bold')

# Plot details
plt.title("Winning Bid vs High Leverage Economy+")
plt.xlabel("High Pressure Economy+")
plt.ylabel("Winning Bid (in crores)")

# Save the plot as an image
output_path = '/Users/siddhantjain/PycharmProjects/NBA Superstars Roles/Winning_Bid_vs_High_Leverage_Economy+.png'
plt.savefig(output_path, dpi=1200, bbox_inches='tight')

# Show the plot
plt.show()
