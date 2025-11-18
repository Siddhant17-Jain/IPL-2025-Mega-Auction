import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr

# Load the IPL Batters data
file_path = '/Files/Batters_vs_Auction.csv'
df = pd.read_csv(file_path)

# Ensure BASRA+, Winning Bid (cr), and BF are numeric (if they are strings, coerce errors)
df['BASRA+'] = pd.to_numeric(df['BASRA+'], errors='coerce')
df['Winning Bid'] = pd.to_numeric(df['Winning Bid'], errors='coerce')
df['BF'] = pd.to_numeric(df['BF'], errors='coerce')

# Filter the data to include only players where Retained = No and BF > 160
df = df[(df['Retained'] == 'No') & (df['BF'] > 160)]

# Drop rows with missing or invalid data
df = df.dropna(subset=['BASRA+', 'Winning Bid'])

# List of players to highlight
highlight_players = ['Rishabh Pant', 'Shreyas Iyer', 'Venkatesh Iyer', 'Jos Buttler', 'KL Rahul']

# Create a mask to filter out the rows for the highlighted players
highlight_mask = df['Player'].isin(highlight_players)

# Calculate and print correlation metrics
pearson_corr, _ = pearsonr(df['BASRA+'], df['Winning Bid'])
spearman_corr, _ = spearmanr(df['BASRA+'], df['Winning Bid'])
print(f"Pearson Correlation: {pearson_corr:.2f}")
print(f"Spearman Correlation: {spearman_corr:.2f}")

# Create the scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x='BASRA+',
    y='Winning Bid',
    hue=highlight_mask,
    palette={True: 'red', False: 'blue'},
    legend=False,
    s=100
)

# Highlight the specific players
for player in highlight_players:
    player_data = df[df['Player'] == player]
    if not player_data.empty:  # Ensure the player is in the filtered dataset
        plt.text(
            player_data['BASRA+'].values[0],
            player_data['Winning Bid'].values[0],
            player,
            horizontalalignment='left',
            size=10,
            color='black',
            weight='bold'
        )

# Set labels and title
plt.title('BASRA+ vs. Winning Bid (Non-Retained Players with BF > 160)', fontsize=14)
plt.xlabel('BASRA+', fontsize=12)
plt.ylabel('Auction Price (cr)', fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()
