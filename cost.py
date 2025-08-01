import pandas as pd
import json
df = pd.read_excel('cross_join_result.xlsx')
with open('station_time.json', 'r') as f:
    dist_dict = json.load(f)
def get_time(row):
    key = f"{row['FROM STTN']}|{row['CRNT_STTN']}"
    rev_key = f"{row['CRNT_STTN']}|{row['FROM STTN']}"
    return dist_dict.get(key) or dist_dict.get(rev_key) or -1  # You can change default 0
df['cost/time'] = df.apply(get_time, axis=1)
output_path = 'final_with_time.xlsx'
df.to_excel(output_path, index=False)

print(f"Final Excel saved at: {output_path}")