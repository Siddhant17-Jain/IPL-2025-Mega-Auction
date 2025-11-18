import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file and specifically the 'High-Leverage+' sheet
file_path = '/Users/siddhantjain/PycharmProjects/NBA Superstars Roles/Files/High-Leverage+.csv'
df = pd.read_csv(file_path)

# Round all numerical values to 2 decimal places
df = df.round(2)

# List of players to highlight
highlight_players = ['Arshdeep Singh', 'Trent Boult', 'Mohammad Siraj', 'Mitchell Starc']

# Create a column to flag if the player is one of the highlighted players
df['highlight'] = df['Player'].apply(lambda x: x in highlight_players)

# Plot: High Leverage Economy+ vs Winning Bid
plt.figure(figsize=(14, 7))
plt.scatter(df['High Leverage Economy+'], df['Winning_Bid'], c=df['highlight'].map({True: 'red', False: 'blue'}), alpha=0.6)

# Highlight the players specifically and add their names on the plot
for player in highlight_players:
    # Check if the player exists in the dataframe
    player_data = df[df['Player'] == player]
    if not player_data.empty:
        plt.scatter(player_data['High Leverage Economy+'], player_data['Winning_Bid'], s=100, edgecolor='black', zorder=5)
        plt.text(player_data['High Leverage Economy+'].values[0], player_data['Winning_Bid'].values[0], player,
                 fontsize=9, ha='right', va='bottom', color='black')

# Plot details
plt.title("Winning Bid vs High Leverage Economy+")
plt.xlabel("High Pressure Economy+")
plt.ylabel("Winning Bid (in crores)")

# Save the plot as an image
output_path = '/Users/siddhantjain/PycharmProjects/NBA Superstars Roles/Winning_Bid_vs_High_Leverage_Economy+ (retained = no).png'
plt.savefig(output_path, dpi=1200, bbox_inches='tight')

# Show the plot
plt.show()
