import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    person.sort_values(by='id',ascending=True,inplace=True)
    person.drop_duplicates(subset=['email'], keep='first', inplace=True)
    return person
    
if __name__ == "__main__":
    data = [[1, 'john@example.com'], [2, 'bob@example.com'], [3, 'john@example.com']]
    person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'Int64', 'email':'object'})
    print(person)
    person = delete_duplicate_emails(person)
    print(person)