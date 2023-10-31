# Task 1: Read the file persona.csv and show general information about the data set.
import pandas as pd
path = "persona.csv"
persona = pd.read_csv(path)
persona.head()

# Task 2: How many unique SOURCEs are there? What is their frequency?
print(f"Count of unique sources: {persona['SOURCE'].nunique()}")
print(f"Their frequency:\n{persona['SOURCE'].value_counts()}")

# Task 3: How many unique PRICEs are there?
print(f"Count of unique PRICE: {persona['PRICE'].nunique()}")

# Task 4: How many sales were realised at which PRICE?
print(f"PRICE frequnecy: \n{persona['PRICE'].value_counts()}")

# Task 5: How many sales from which country?
print(f"COUNTRY frequnecy: \n {persona['COUNTRY'].value_counts()}")

# Task 6: How much was earned from sales by country?
print(persona.groupby(['COUNTRY'])['PRICE'].agg(['sum']))

# Task 8: What are the PRICE averages by country?
print(persona.groupby(['COUNTRY'])['PRICE'].agg(['mean']))

# Task 9: What are the PRICE averages by SOURCEs?
print(persona.groupby(['SOURCE'])['PRICE'].agg(['mean']))

# Task 10: What are the PRICE averages by COUNTRY-SOURCE?
print(persona.groupby(['COUNTRY', 'SOURCE'])['PRICE'].mean())
