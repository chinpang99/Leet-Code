import pandas as pd
import numpy as np

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    employee_copy = employee.copy()
    final_df = employee.merge(employee_copy, how='inner', left_on='managerId', right_on=['id'])
    final_df['compare'] = np.where(final_df['salary_x']>final_df['salary_y'], final_df['name_x'], None)
    final_df_v2 = pd.DataFrame()
    final_df_v2['Employee'] = final_df['compare']
    final_df_v2 = final_df_v2.dropna()
    return final_df_v2

def find_employees_optimized(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(right = employee, how = 'left', left_on = 'managerId', right_on = 'id')
    emp = df[df['salary_x'] > df['salary_y']]['name_x']

    return pd.DataFrame({'Employee': emp})

if __name__ == "__main__":
    data = [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]]
    employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'managerId':'Int64'})

    final_df = find_employees(employee)
    print(final_df)
