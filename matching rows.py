import pandas as pd
df = pd.read_excel('final_with_time_cleaned_file.xlsx')
df_filtered = df[df['INDENTED TYPE'] == df['RTYPE']]
df_filtered.to_excel('filtered_matching_rakes.xlsx', index=False)
print("Filtered rows saved to 'filtered_matching_rows.xlsx'")
