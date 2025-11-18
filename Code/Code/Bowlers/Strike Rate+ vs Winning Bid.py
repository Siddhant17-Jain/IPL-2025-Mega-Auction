import pandas as pd
import matplotlib.pyplot as plt

# Load the Strike Rate+.csv file
file_path = '/Users/siddhantjain/PycharmProjects/NBA Superstars Roles/Files/Strike Rate+.csv'
df = pd.read_csv(file_path)

# List of players to highlight
highlight_players = ['Arshdeep Singh', 'Trent Boult', 'Mohammad Siraj', 'Mitchell Starc']

# Create a column to flag if the player is one of the highlighted players
df['highlight'] = df['Player'].apply(lambda x: x in highlight_players)

# Plot: Strike Rate+ vs Winning Bid
plt.figure(figsize=(14, 7))
plt.scatter(df['Strike Rate+'], df['Winning_Bid'], c=df['highlight'].map({True: 'red', False: 'blue'}), alpha=0.6)

# Highlight the players specifically and add their names (bolded) on the plot
for player in highlight_players:
    # Check if the player exists in the dataframe
    player_data = df[df['Player'] == player]
    if not player_data.empty:
        plt.scatter(player_data['Strike Rate+'], player_data['Winning_Bid'], s=100, edgecolor='black', zorder=5)
        plt.text(player_data['Strike Rate+'].values[0], player_data['Winning_Bid'].values[0],
                 f"{player}", fontsize=9, ha='right', va='bottom', color='black', fontweight='bold')

# Plot details
plt.title("Winning Bid vs Strike Rate+")
plt.xlabel("Strike Rate+")
plt.ylabel("Winning Bid (in crores)")

# Save the plot as an image
output_image_path = '/Users/siddhantjain/PycharmProjects/NBA Superstars Roles/Winning_Bid_vs_Strike_Rate+.png'
plt.savefig(output_image_path, dpi=1200, bbox_inches='tight')

# Show the plot
plt.show()

print(f"Plot saved to: {output_image_path}")
