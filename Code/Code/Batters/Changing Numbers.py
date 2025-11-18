import pandas as pd

# Load the CSV file
file_path = '/Files/IPL_2025_Auction.csv'
df = pd.read_csv(file_path)

# Modify the 'Base Price' and 'Winning Bid' columns
df['Base Price (cr)'] = df['Base Price'] / 10**7
df['Winning Bid (cr)'] = df['Winning Bid'] / 10**7

# Drop the old columns
df.drop(['Base Price', 'Winning Bid'], axis=1, inplace=True)

# Sort the DataFrame by 'Winning Bid (cr)'
df = df.sort_values(by='Winning Bid (cr)', ascending=False)  # Change to True for ascending order

# Save the updated DataFrame back to a CSV file
df.to_csv('IPL_2025_Auction_Updated.csv', index=False)

print("File updated, sorted by 'Winning Bid (cr)', and saved as 'IPL_2025_Auction_Updated.csv'")
