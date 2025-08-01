import pandas as pd
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary

df = pd.read_excel("filtered_matching_rakes.xlsx")
df.columns = df.columns.str.strip()
df = df[['Demand_Unit', 'ID', 'cost/time']]

demand_units = df['Demand_Unit'].unique()
ids = df['ID'].unique()
costs = {(row['Demand_Unit'], row['ID']): row['cost/time'] for _, row in df.iterrows()}

prob = LpProblem("Optimal_Assignment", LpMinimize)
x = LpVariable.dicts("assign", (ids, demand_units), cat=LpBinary)

prob += lpSum(x[i][d] * costs.get((d, i), 0) for d in demand_units for i in ids)

for d in demand_units:
    prob += lpSum(x[i][d] for i in ids if (d, i) in costs) == 1

for i in ids:
    prob += lpSum(x[i][d] for d in demand_units if (d, i) in costs) <= 1

prob.solve()

assignments = [(d, i) for d in demand_units for i in ids if x[i][d].varValue == 1]
result_df = pd.DataFrame(assignments, columns=['Demand_Unit', 'Assigned_ID'])
result_df['cost/time'] = result_df.apply(lambda row: costs[(row['Demand_Unit'], row['Assigned_ID'])], axis=1)

result_df.to_excel("optimal_assignment_result.xlsx", index=False)
