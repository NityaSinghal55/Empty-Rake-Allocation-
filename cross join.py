import pandas as pd
df1 = pd.read_excel('final_demand.xlsx')
df2 = pd.read_excel('empty_info.xlsx')
df1['key'] = 1
df2['key'] = 1
cross_joined = pd.merge(df1, df2, on='key').drop('key', axis=1)
output_path = 'cross_join_result.xlsx'
cross_joined.to_excel(output_path, index=False)

print(f"Cross join File saved at: {output_path}")
