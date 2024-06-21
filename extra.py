import pandas as pd

# Sample data for demonstration purposes

df = pd.read_excel(r'/Users/stephencox/Downloads/3 week pickup.xlsx')

beta = 0.03

# Initialize the Trend column
df['Trend'] = 0.0

# Calculate the initial trend based on provided formula
for i in range(1, len(df)):
    todays_level = df.at[i, 'Level']
    yesterdays_level = df.at[i - 1, 'Level']
    yesterdays_trend = df.at[i - 1, 'Trend']
    df.at[i, 'Trend'] = beta * (todays_level - yesterdays_level) + (1 - beta) * yesterdays_trend

print(df)