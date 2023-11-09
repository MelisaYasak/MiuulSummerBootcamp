# -*- coding: utf-8 -*-
"""
#Return on Lead Calculation with Rule-Based Classification

##Job Problem

A game company uses some of the characteristics of its customers to create new level-based customer personas, and to create new customer personas for these new customer personas.
According to these segments, the company wants to create segments and estimate how much new customers can earn the company on average according to these segments.
For example:
It is desired to determine how much a 25-year-old male IOS user from Turkey can earn on average.
"""


# Task 1: Read the file persona.csv and show general information about the data set.
import pandas as pd

persona = pd.read_csv("/persona.csv")
print(f"PERSONA INFO:\n{persona.info()}\n#############\nPERSONA HEAD: {persona.head()}\n#############\nPERSONA TAIL:\n{persona.tail()}\n#############\nPERSONA DESCRIBE:\n{persona.describe().T}\n#############\nPERSINA SHAPE:\n{persona.shape}\n#############\nPERSONA COLUMNS:\n{persona.columns}\n#############\nPERSONA INDEX:\n{persona.index}\n#############\nPERSONA'S NULL VALUES:\n{persona.isnull().values.any()}")

persona[['PRICE', 'AGE']].corr()

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

# Task 7: What is the number of sales by SOURCE types?
persona.SOURCE.value_counts()

# Task 8: What are the PRICE averages by country?
print(persona.groupby(['COUNTRY'])['PRICE'].agg(['mean']))

# Task 9: What are the PRICE averages by SOURCEs?
print(persona.groupby(['SOURCE'])['PRICE'].agg(['mean']))

# Task 10: What are the PRICE averages by COUNTRY-SOURCE?
print(persona.groupby(['COUNTRY', 'SOURCE'])['PRICE'].mean())

# Task 2: What are the average earnings by COUNTRY, SOURCE, SEX, AGE?
result = persona.groupby(['COUNTRY', 'SOURCE', 'SEX', 'AGE'])['PRICE'].mean()
print(result)

# Task 3: Sort the output by PRICE.
agg_df = result.sort_values(ascending=False)
print(agg_df)

# Task 4: Convert the names in the index into variable names.
reset_ind_df = agg_df.reset_index()
print(reset_ind_df)
print(reset_ind_df.columns)

# Task 5: Convert age into a categorical variable and add it to agg_df.
age_groups = {
    (0, 18): '0_18',
    (19, 23): '19_23',
    (24, 30): '24_30',
    (31, 40): '31_40',
    (41, 70): '41_70'
}

reset_ind_df['AGE_CAT'] = reset_ind_df['AGE'].apply(
    lambda age: next((
        category for group, category in age_groups.items() if age in range(group[0], group[1] + 1)), None))
print(reset_ind_df)

# Task 6: Define new level-based customers (persona).
reset_ind_df['costumers_level_based'] = [f"{country.upper()}_{source.upper()}_{sex.upper()}_{age_cat.upper()}" for country, source, sex, age_cat in zip(reset_ind_df['COUNTRY'], reset_ind_df['SOURCE'], reset_ind_df['SEX'], reset_ind_df['AGE_CAT'] )]
print(reset_ind_df)

df = reset_ind_df[['costumers_level_based', 'PRICE']].copy()
print(df)

# After the customers_level_based values are created, these values must be deduplicated.
unique_df = df.groupby('costumers_level_based')['PRICE'].mean().reset_index()
print(unique_df)

unique_df['PRICE'].describe()

# Task 7: Divide new customers (personas) into segments.
unique_df['price_segment'] = pd.qcut(df.PRICE, q=4, labels=['D', 'C','B', 'A'])
print(unique_df['price_segment'].unique())
unique_df.head()

# Describe the segments (group by segments and get price mean, max, sum).
describe_df= unique_df.groupby(['price_segment'])['PRICE'].agg(['sum', 'mean', 'max'])
#unique_df.groupby('price_segment').agg({'PRICE': 'mean'}).reset_index()
print(describe_df.reset_index())

# Task 8: Categorise new customers and estimate how much revenue they can generate.

# QUESTION 1: Which segment does a 33-year-old Turkish woman using ANDROID belong to and how much income is she expected to earn on average?
print(unique_df[unique_df['costumers_level_based']=='TUR_ANDROID_FEMALE_31_40'])
# QUESTION 2: Which segment does a 35-year-old French woman using IOS belong to and how much income can she be expected to earn on average?
print(unique_df[unique_df['costumers_level_based']=='BRA_ANDROID_FEMALE_0_18'])

