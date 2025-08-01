#  Optimal Empty Rake Allocation in Indian Railways

This project demonstrates a complete data processing and optimization pipeline for **intelligent allocation of empty rakes to meet demand units** in Indian Railways. It uses **Python, Pandas**, and **Linear Programming (PuLP)** to minimize cost or time between origin and destination stations.

---

##  Objective

To automate and optimize the assignment of available empty rakes to rake demands based on:
- Station-to-station travel time or cost
- Matching rake types
- Minimizing overall transportation time

---

##  Technologies Used

- Python 3
- Jupyter Notebook
- pandas
- PuLP (for Linear Programming)
- Excel (input/output)
- JSON (for station travel times)

---

##  Input Files

| File Name            | Description                                  |
|---------------------|----------------------------------------------|
| `final_demand.xlsx` | Contains demand unit data                    |
| `empty_info.xlsx`   | Contains available empty rake info           |
| `station_time.json` | Dictionary with travel time between stations |

---

##  Process Overview

1. **Cross Join:**  
   All combinations of demand units and available rakes are generated.

2. **Add Travel Time (cost/time):**  
   Adds a travel time/cost column between current station and demand station using a JSON dictionary.

3. **Filter Invalid Rows:**  
   Removes pairs without travel time information (i.e., cost = -1).

4. **Match Rake Type:**  
   Filters pairs where `RTYPE` matches the `INDENTED TYPE`.

5. **Optimization:**  
   Uses **binary linear programming** to:
   - Assign one rake to each demand
   - Ensure no rake is assigned more than once
   - Minimize total cost/time

6. **Save Output:**  
   Final assignments and their cost are saved to `optimal_assignment_result.xlsx`.

---

##  Output Files

| File Name                        | Description                                   |
|----------------------------------|-----------------------------------------------|
| `cross_join_result.xlsx`         | All possible demand-rake pairs                |
| `final_with_time.xlsx`           | Pairs with time/cost info                     |
| `final_with_time_cleaned_file.xlsx` | Invalid pairs removed                        |
| `filtered_matching_rakes.xlsx`   | Pairs with matching rake type                |
| `optimal_assignment_result.xlsx` | Final result with optimal rake assignments    |

