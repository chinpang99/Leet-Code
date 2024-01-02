import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    results = pd.DataFrame()
    results = person.loc[person.duplicated(subset=['email']), ['email']]
    return results.drop_duplicates()

    

if __name__ == "__main__":
    data = [[1, 'a@b.com'], [2, 'c@d.com'], [3, 'a@b.com']]
    person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'Int64', 'email':'object'})
    final_df = duplicate_emails(person)
    print(final_df)