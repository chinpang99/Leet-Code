import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by='recordDate', inplace=True)
    # Step 1: Calculate the difference in temperature from the previous day and 
    # check if it is greater than 0 (indicating a rise in temperature).
    temp_increase = weather['temperature'].diff() > 0
    
    # Step 2: Calculate the difference in days between each record and 
    # check if it is exactly 1 day (indicating consecutive days).
    consecutive_days = weather['recordDate'].diff().dt.days == 1
    
    # Step 3: Combine the two conditions using & (logical AND) to select rows 
    # where both conditions are true (temperature increased on consecutive days).
    # Then, select only the 'id' column of these rows.
    result = weather[temp_increase & consecutive_days][['id']]
    
    # Step 5: Return the result as a DataFrame.
    return result
    
if __name__=="__main__":
    data = [[1,'2015-01-01',10], [2,'2015-01-02',25],[3,'2015-01-03',20],[4,'2015-01-04',30]]
    weather=pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype({'id':'int64', 'recordDate':'datetime64[ns]', 'temperature':'int64'})
    result=rising_temperature(weather)
    # print(result)