import pandas as pd
df = pd.read_excel('final_with_time.xlsx')
df_cleaned = df[df['cost/time'] != -1]
df_cleaned.to_excel('final_with_time_cleaned_file.xlsx', index=False)
print("Rows with -1 removed and new file saved as 'cleaned_file.xlsx'")
