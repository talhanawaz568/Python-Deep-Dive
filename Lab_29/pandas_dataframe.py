import pandas as pd
df = pd.read_csv('/root/filesystem/home/ubuntu/labs/Lab_29/read.csv')
print(df.head())


filtered_df = df[df['Age'] > 30]
print(filtered_df.head())
filtered_df.to_csv('filtered_data.csv', index=False)
