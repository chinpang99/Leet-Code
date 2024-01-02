import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Select the customers whose 'id' is not present in the orders DataFrame's 'customerId' column.
    df = customers[~customers['id'].isin(orders['customerId'])]

    # Build a DataFrame that only contains the 'name' column and rename it as 'Customers'.
    df = df[['name']].rename(columns={'name': 'Customers'})

    return df

    

if __name__ == "__main__":
    data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
    customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
    data = [[1, 3], [2, 1]]
    orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})

    final_df = find_customers(customers, orders)
    print(final_df)