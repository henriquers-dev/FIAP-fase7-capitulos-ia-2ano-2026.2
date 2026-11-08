import pandas as pd

df = pd.read_csv("log.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.sort_values(by=['case_id', 'timestamp'])
