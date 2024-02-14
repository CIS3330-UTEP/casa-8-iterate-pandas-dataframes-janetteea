# Method 4, using iterrows() 

# Import pandas package as pd
import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')

# Method 4:  Using iterrows()

for i,row in df.iterrows():
    print (row['date'],
           row['currency_code'],
           row['name'],
           row['dollar_ex'],
           row['dollar_price']) 
    
# Method 6:  Using apply()

print (df.apply(lambda row: (row['date'], row['name'], row['dollar_price']), axis = 1))


    


